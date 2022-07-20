from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def django_course(request):
    return HttpResponse("<h1>Hello World</h1>")
    
