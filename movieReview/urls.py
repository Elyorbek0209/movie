from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_movie/$', views.addMovie, name='add_movie'),
]
