from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('payment/', views.payment, name='payment'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
]