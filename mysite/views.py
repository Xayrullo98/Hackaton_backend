from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def project(request):
    return render(request, 'index.html')


def article(request):
    return render(request, 'index.html')


def mentor(request):
    return render(request, 'index.html')


def event(request):
    return render(request, 'index.html')
