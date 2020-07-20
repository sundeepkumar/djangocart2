# sendemail/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import url


from .views import emailView

urlpatterns = [
    url(r'^email/(?P<pk>\d+)/$', emailView, name='email'),
    #path('success/', successView, name='success'),
]