from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def msd(request):
    return render(request, 'msd.html')

def raina(request):
    return HttpResponse('<center><h1>Mr IPL</h1></center>')