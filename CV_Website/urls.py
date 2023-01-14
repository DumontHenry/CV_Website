from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.CV_Web, name='CV'),
    path("upload", views.UploadFile, name="UploadFile"),
    path("success/", views.redirect_email, name='email_sent'),
]
