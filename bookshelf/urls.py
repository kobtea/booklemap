from django.conf.urls import patterns, url
from .views import Search, List
import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^search/', Search.as_view(), name='search'),
    url(r'^list/', List.as_view(), name='list'),
)
