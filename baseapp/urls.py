from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('obtain_word', obtain_word, name='obtain_word'),
    path('', mi_vista, name='mi_vista'),

    ]
