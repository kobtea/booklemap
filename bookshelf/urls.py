from django.conf.urls import patterns, url
import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
)
