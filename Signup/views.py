from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render,render_to_response
from django.views.decorators.csrf import csrf_exempt
from .forms import RegistrationForm
from .models import *


def registration_details(request):
    data_model = User.objects.all()
    for i in data_model:
        print(i.username)
        print(i.password)
        print(i.first_name)
        print(i.last_name)
        print(i.email)

    return render_to_response('Data.html', {'data': data_model})

@csrf_exempt

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(form)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            User.objects.create_user(username=username, password = password, first_name=first_name, last_name=last_name, email=email)
            return HttpResponseRedirect('/signup/')
    else:
        form = RegistrationForm()
    return render(request,'signup.html', {'form1': form})

