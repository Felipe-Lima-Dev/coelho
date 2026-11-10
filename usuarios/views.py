from django.shortcuts import render

def login(request):
    return render(request, 'usuarios/login')

def register(request):
    return render(request, 'usuarios/register')
