from django.forms import ModelForm
from django import forms
from .models import *
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import validate_email


class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Username', error_messages={'Required': 'Please enter Username'})
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput(),
                                error_messages={'Required': 'Password should be minimum 8 characters'})
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput())
    first_Name = forms.CharField(label='First Name', error_messages={'Required':'Please enter First Name'})
    last_Name = forms.CharField(label='Last Name', error_messages={'Required': 'Please enter Last Name'})
    email = forms.EmailField(label='Email', error_messages={'Required': 'Please enter Email'})


    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 == password2:
            return password2
        else:
            raise forms.ValidationError("Passwords do not match")

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+\d', username):
            raise forms.ValidationError("Username can only contain characters and digits")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Username is already taken")


    def clean_email(self):
        email = self.cleaned_data("email")
        try:
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError("Email already registered")

        try:
            CorrectEmail = validate_email(email)
        except:
            return forms.ValidationError("Email format is not correct")
        return CorrectEmail

    def clean_number(self):
        number = self.cleaned_data("ContactNumber")
        if not re.search(r'^[2-9]{1}[0-9]{9}$', ):
            raise forms.ValidationError("Invalid Contact Number")
        else:
            return number

    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'first_name',
                  'last_name',
                  'email',
                  ]

