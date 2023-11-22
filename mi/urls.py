from mi.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('rohit/', rohit, name='rohit'),
    path('bumrah/', bumrah, name='bumrah'),
]