
from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^', views.registration_details),
    url(r'^signup/$', views.register),
]