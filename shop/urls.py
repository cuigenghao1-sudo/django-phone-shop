from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('phones/', views.phones, name='phones'),
    path('phones/1/', views.phone_detail, name='phone_detail'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
]