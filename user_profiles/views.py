# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User

from user_profiles.models import SalesPerson
from user_profiles.forms import UserForm

def signup_view(request):
    dict = {}
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if len(str(data['contact_number']))==10:
                form.save()
                salesperson = SalesPerson()
                salesperson.contactNumber = data['contact_number']
                salesperson.user =User.objects.get(username = data['username'])
                salesperson.save()
                messages.add_message(request, messages.INFO, " You have successfully registered. You can sign in now.")
                return (redirect(reverse('Login:login')))
            else:
                messages.add_message(request, messages.ERROR, " enter a valid phone number")
    else:
        form = UserForm()
    dict['form'] = form
    return render_to_response('signup/signup.html',dict,context_instance=RequestContext(request))

def login_view(request):
    state="please login"
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                if user.is_superuser:
                        return(redirect(reverse('Login:admin_home')))
                else:
                    response = redirect(reverse('Login:user_home'))
                return(response)
            else:
                state = "Your account is not active, please contact the admin"
        else:
            state = "Your username and/or password were incorrect"
    messages.add_message(request, messages.ERROR, state)
    return render_to_response('login/login.html',context_instance=RequestContext(request))

def user_view(request):
    if request.user.is_authenticated():
        return render_to_response('home/home.html')
    else:
        return(redirect(reverse('Login:login')))

def admin_view(request):
    if request.user.is_authenticated() and request.user.is_staff:
        return render_to_response('home/adminhome.html')

def logout_view(request):
    return logout_then_login(request,login_url='/')