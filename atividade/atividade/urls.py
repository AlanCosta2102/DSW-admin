from django.urls import path
from exercicio import views

urlpatterns = [
    path('',views.index),
]