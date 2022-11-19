from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    name = request.GET['name']
    message = request.GET['message']
    return render(request, 'hello.html', {'name': name, 'message': message})


def home(request):
    return render(request, 'main.html')
