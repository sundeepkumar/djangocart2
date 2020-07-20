# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.contrib.auth.models import User
from posts.models import Post
from django.conf import settings
from django.contrib import messages



def emailView(request , pk=None):
    current_user_email = request.user.email
    #user_edit = get_object_or_404(UserProfile, pk=current_user)
    current_user = request.user
    results = Post.objects.filter(pk=pk)
    for post in results:
        current_item = post.title

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            message_plus = 'Hi, you recived a message from ' + str(current_user) + ', a futre buyer about the ' + str(current_item) + '. Here is the user\'s message:\n \n' + form.cleaned_data['message']
            message_final = message_plus + '\n \nThe user\'s email is: ' + str(current_user_email)
            subject = 'A message from a futre buyer (C-2319)'
            from_email = settings.EMAIL_HOST_USER
            message = message_final
            try:
                send_mail(subject, message, from_email, [post.user.email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            message_plus_cc = 'Hi, you have sent a message about ' + str(current_item) + '.'
            message_final_cc = message_plus_cc + '\n\n\nHere is a copy of your message:\n\n' + form.cleaned_data['message']
            subject_cc = 'You have sent a meesgae about an Item - C-2319'
            message_cc = message_final_cc
            try:
                send_mail(subject_cc, message_cc, from_email, [current_user_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            messages.success(request, 'Your email was successfully sent!', extra_tags='send')
            return redirect('/post/' + str(pk))

    return render(request, "email.html", {'form': form})

#def successView(request):
#    return HttpResponse('Success! Thank you for your message.')