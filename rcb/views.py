from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def virat(request):
    return render(request, 'virat.html')

def siraj(request):
    return HttpResponse('<center><h1>Mia Magic</h1></center>')