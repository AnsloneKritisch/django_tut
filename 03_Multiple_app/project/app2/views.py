from django.http import HttpResponse
from django.shortcuts import render

def django_app2(request):
    return HttpResponse("Hello World From app2 ")

