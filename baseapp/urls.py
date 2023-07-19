from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('pdf_word_get/', receive_data_get, name='receive_data_get'),
   
]
