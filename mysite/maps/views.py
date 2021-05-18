from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Овде ќе ја ставиме нашата мап со центар на ПД Голубац!")
