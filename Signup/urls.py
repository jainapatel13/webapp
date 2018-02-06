
from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^homepage', views.registration_details),
    url(r'^', views.register),
]