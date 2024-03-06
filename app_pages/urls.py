from django.urls import path
from .views import *

urlpatterns = [
    path('first/', first, name='first'),
    path('second/', second, name='second'),
    path('third/', third, name='third'),
    path('fourth/', fourth, name='fourth'),
    path('last/', last, name='last')
]