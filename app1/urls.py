from django.urls import path
from app1.views import *

app_name='question'

urlpatterns=[
    path('naruto/',naruto,name='naruto')
]