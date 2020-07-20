from django.conf.urls import url
from . import views
from .views import PostDetailView, PostListView, ForSaleListView
from django.urls import path , re_path



urlpatterns = [
    url('add/post/$' , views.add_post , name='add_post'),
    re_path(r'^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
    url(r'^edit/(?P<pk>\d+)/$' , views.edit_post, name = 'edit_post'),
    path('forsale' , ForSaleListView.as_view(), name='for_sale'),
    url(r'^delete/(?P<pk>\d+)/$' , views.delete_post, name = 'delete_post'),
    #re_path(r'^(?P<pk>\d+)/$', views.contact_p, name="contact_p"),
    #path('', home.views.home, name='home'),
    ]
