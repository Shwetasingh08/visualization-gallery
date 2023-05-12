from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reply/', views.predict, name='predict')
]