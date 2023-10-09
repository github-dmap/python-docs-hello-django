from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hi HPE Team good evening, we are learning Azur cloud computing. My name is Arun")
