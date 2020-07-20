from . import views
from .views import view_profile , edit_profile , change_password
from django.urls import path, re_path
from django.conf.urls import url


urlpatterns = [
    # url(r'^$', views.home),
    url(r'^profile/$', views.view_profile, name="view_profile"),
    url(r'^profile/edit/$' , views.edit_profile, name = 'edit_profile'),
    url(r'^change-password$' , views.change_password, name = 'change_password'),
    url(r'^delete/$', views.remove_user, name= "remove_user"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
