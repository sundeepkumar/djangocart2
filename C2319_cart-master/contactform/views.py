from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.

def index(request):

    if request.method == "POST":
        message = request.POST['message']
        send_mail(
          'Contact Form' ,
          message,
          settings.EMAIL_HOST_USER , 
          [user.email],
          fail_silently = False)
    return render (request , 'contact/contact_page.html')