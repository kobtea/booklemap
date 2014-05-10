from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from .libs import amazon
from .models import Status


def index(request):
    return render(request, 'bookshelf/index.html', {})


class Search(View):
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        item_dict = amazon.api.find_by_keyword(q)
        for i in range(0, len(item_dict)):
            status = None
            try:
                status = Status.objects.get(
                    user=request.user.id,
                    asin=item_dict[i]['asin']).status
            except Status.DoesNotExist:
                pass
            item_dict[i]['status'] = status
        meta = {'aso_tag': amazon.api.associate_tag}
        # TODO: no matches handling
        return render(request,
                      'bookshelf/search.html',
                      {'item_dict': item_dict,
                       'meta': meta}
                      )

    def post(self, request, *args, **kwargs):
        asin = request.POST['asin']
        status = request.POST['status']
        user = request.user.id
        # TODO: refactor with get_or_create
        try:
            status_obj = Status.objects.get(user=user, asin=asin)
            status_obj.status = status
        except Status.DoesNotExist:
            status_obj = Status(
                user=user,
                asin=asin,
                status=status
            )
        status_obj.save()
        # TODO: refactor me
        return redirect(request.META['HTTP_REFERER'])


class List(View):
    def get(self, request, *args, **kwargs):
        status_list = Status.objects.filter(user=request.user.id)
        l = []
        for status in status_list:
            d = {}
            d['status'] = status.status
            d['asin'] = status.asin
            having_user_id = [x.user for x in Status.objects
                              .filter(asin=status.asin)
                              .exclude(user=request.user.id)]
            username_list = []
            for user_id in having_user_id:
                username_list.append(User.objects.get(pk=user_id).username)
            d['having'] = username_list
            l.append(d)

        meta = {'aso_tag': amazon.api.associate_tag}
        return render(request,
                      'bookshelf/list.html',
                      {'item_list': l,
                       'meta': meta}
                      )
