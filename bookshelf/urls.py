from django.conf.urls import patterns, url
from .views import Search
import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^search/', Search.as_view(), name='search'),
)
