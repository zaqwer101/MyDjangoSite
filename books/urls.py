from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^authors/(?P<a_id>[0-9]+)/$', views.author_detail, name='author_detail'),
    url(r'^(?P<b_id>[0-9]+)/$', views.book_detail, name='book_detail'),
]