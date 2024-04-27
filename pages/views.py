from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def location(request):
    return render(request, 'pages/location.html')


def about(request):
    return render(request, 'pages/about.html')

