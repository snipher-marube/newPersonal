from django.urls import path
from .import views
from django.contrib import admin

urlpatterns = [
    path('newsletter/', views.newsletter, name='newsletter'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),

]


