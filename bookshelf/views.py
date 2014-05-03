from django.shortcuts import render
from .libs import amazon


def index(request):
    return render(request, 'bookshelf/index.html', {})


def search(request):
    q = request.GET.get('q')
    item_dict = amazon.api.find_by_keyword(q)
    meta = {'aso_tag': amazon.api.associate_tag}
    # TODO: no matches handling
    return render(request,
                  'bookshelf/list.html',
                  {'item_dict': item_dict,
                   'meta': meta}
                  )
