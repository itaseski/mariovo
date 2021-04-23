from django.shortcuts import render


def home(request):
    return render(request, 'vilages/home.html')


def index(request):
    return render(request, 'vilages/index.html')
