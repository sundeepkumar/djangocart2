from django.shortcuts import render, redirect, get_object_or_404
from .forms import(
    RegisterForm,
    UserProfileForm,
    EditProfileForm,
    EditProfileFormCustme,
    RemoveUser,
)
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash , get_user_model , login
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        profile_form = UserProfileForm(response.POST)
        if form.is_valid() and profile_form.is_valid():
            # form.save()
            n = form.cleaned_data["email"]
            if not n.lower().endswith('.edu'):
                # raise forms.ValidationError('Only .edu email addresses allowed')
                messages.success(response, 'Only .edu email addresses allowed! Please try again with a valid email address.', extra_tags='email_not_edu')
                context = {'form' : form, 'profile_form' : profile_form}
                return render(response, 'register/register.html' , context)

            if User.objects.filter(email=n).exists():
                messages.success(response, 'A user with that email address already exists', extra_tags='email_not_uni')
                context = {'form' : form, 'profile_form' : profile_form}
                return render(response, 'register/register.html' , context)
            user = form.save(commit=False)
            profile = profile_form.save(commit=False)
            profile.user = user
            user.is_active = False
            profile.is_active = False
            user.save()
            profile.save()

            current_site = get_current_site(response)
            mail_subject = 'Activate your College Market account.'
            message = render_to_string('register/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            # return HttpResponse('Please confirm your email address to complete the registration')
            messages.success(response, 'We have sent you an email. Please confirm your email address to complete the registration', extra_tags='email_active')
            return redirect('/')



            # login(response , user)

            # subject = "Welcome to C-2319 (College Market)"
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [user.email]
            # message = """Welcome to College Market, the best way to buy and sell stuff online to other students, staff and faclty members."""
            # send_mail(subject , message , email_from , recipient_list)
            # messages.success(response, 'Your account has been created successfully!', extra_tags='account_create')
            # return redirect('/')
    else:
        form = RegisterForm()
        profile_form = UserProfileForm()
    context = {'form' : form, 'profile_form' : profile_form}
    return render(response, 'register/register.html' , context)

def activate(response, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(response, user)
        # return redirect('home')
        messages.success(response, 'Welcome to College Market!', extra_tags='email_active_true')
        return redirect('/')
    else:
        return HttpResponse('Activation link is invalid!')

def edit_profile(response , pk=None):
    current_user = response.user.userprofile.pk
    user_edit = get_object_or_404(UserProfile, pk=current_user)

    if response.method == 'POST':
        form_e = EditProfileForm(response.POST , instance=response.user)
        profile_form_e = UserProfileForm(response.POST , instance=user_edit)
        if form_e.is_valid() and profile_form_e.is_valid():
            user = form_e.save()
            profile = profile_form_e.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(response, 'Your information has been updated successfully!', extra_tags='info_update')
            return redirect('/account/profile')
    else:
        form_e = EditProfileForm(instance=response.user)
        profile_form_e = UserProfileForm(instance=user_edit)
    context = {'form_e' : form_e , 'profile_form_e' : profile_form_e , 'user_edit' : user_edit}
    return render(response, 'registration/edit_profile.html' , context)

def remove_user(response , pk=None):
    if response.method == 'POST':
        item = get_object_or_404(User , pk=pk)
        rem = User.objects.get(username=form.cleaned_data['username'])
        User.delete()
        return redirect('/post/')

    else:
        form = RemoveUser()
    context = {'form': form}
    return render(response, 'registration/remove_user.html', context)



def change_password(response):
    if response.method == 'POST':
        form = PasswordChangeForm(data=response.POST, user=response.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(response , form.user)
            messages.success(response, 'Your password has been updated successfully!', extra_tags='password_update')
            return redirect('/account/profile')
        else:
            return redirect('/account/-change-password')
    else:
        form = PasswordChangeForm(user=response.user)
        context = {'form' : form}
        return render(response, 'registration/change_password.html', context)




def view_profile(response):
    storage = messages.get_messages(response)
    args = {'user' : response.user , 'message' : storage}
    return render (response, 'registration/profile.html' , args)
