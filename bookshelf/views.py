from django.shortcuts import render
from django.views.generic import View
from .libs import amazon
from .models import Status

from django.http import HttpResponse


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
                    asin=item_dict[i]['asin'])
            except Status.DoesNotExist:
                pass
            item_dict[i]['status'] = status
        meta = {'aso_tag': amazon.api.associate_tag}
        # TODO: no matches handling
        return render(request,
                      'bookshelf/list.html',
                      {'item_dict': item_dict,
                       'meta': meta}
                      )

    def post(self, request, *args, **kwargs):
        # import pprint
        # pp = pprint.PrettyPrinter(indent=4).pprint
        asin = request.POST['asin']
        status = request.POST['status']
        user = request.user.id
        try:
            status = Status.objects.get(user=user, asin=asin)
        except Status.DoesNotExist:
            status = Status(
                user=user,
                asin=asin,
                status=status
            )
        status.save()
        return HttpResponse('hoge')
