from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import views

def password_reset(request):
    response = views.password_reset(request=request,template_name='password_reset/password_reset_form.html',
                   email_template_name='password_reset/password_reset_email.html',
                   subject_template_name='password_reset/password_reset_subject.txt',
                   password_reset_form=PasswordResetForm,
                   token_generator=default_token_generator,
                   post_reset_redirect=reverse("PasswordReset:password_reset_done"),
                   from_email=None,
                   current_app=None,
                   extra_context=None)
    return response
    #dict = {}
    #if request.POST:
    #   form = PasswordResetForm(request.POST)
    #   if form.is_valid():
    #       messages.add_message(request, messages.INFO, " submitted for reset. Please check your inbox.")
    #       
    #   else:
    #       messages.add_message(request, messages.ERROR, " Enter email!")
    #dict['form'] = PasswordResetForm
    #return render_to_response('password_reset/password_reset_form.html',dict,context_instance=RequestContext(request))

def password_reset_confirm(request,uidb36,token):
    dict = {}
    dict['uidb36'] = uidb36
    dict['token'] = token
    return render_to_response('password_reset/password_reset_confirm.html ',dict,context_instance=RequestContext(request))

def password_reset_done(request):
    response = views.password_reset_done(request=request,
                        template_name='password_reset/password_reset_done.html',
                        current_app=None, extra_context=None)
    return response
    #return render_to_response('password_reset/password_reset_confirm.html ')# Create your views here.
