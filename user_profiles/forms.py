from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm (UserCreationForm):
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    contact_number = forms.DecimalField(required = True, max_digits = 10, decimal_places = 0)
    
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','contact_number')