from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the logs index.")

def sessions(request):
    return HttpResponse("Hello, world. You're at the sessions page.")

def exercises(request):
    return HttpResponse("Hello, world. You're at the exercises page.")

def performance_progress(request):
    return HttpResponse("Hello, world. You're at the performance progress page.")
