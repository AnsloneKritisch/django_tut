from django.http import HttpResponse
from django.shortcuts import render

def django_app1(request):
    return HttpResponse("Hello World From app1 ")

