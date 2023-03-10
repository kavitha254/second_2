from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def kavi(request):
    return HttpResponse('<marquee><h1>kavitha is good girl</h1></marquee>')

def rocky(request):
    return HttpResponse('<marquee><h1>Rakesh and kavitha both are good friends</h1></marquee>')

def manu(request):
    return HttpResponse('<marquee><h1>kavi manu sujji josh best friends forever</h1></marquee>')

def satti(request):
    return HttpResponse('<marquee><h1>you are the cutest Brother in this world Always were and always will be i love you brother</h1></marquee> ')


def ramya(request):
    return HttpResponse('<h1>Ramya and kavitha both are good best frends forever</h1>')

def mahadev(request):
    return HttpResponse('<marquee><h1>Everyone says monday is your day But for me everyday is your day MAHADEV.</h1></marquee>')

def kavi(request):
    return HttpResponse('<marquee><h1>Keep Working For Your Dreams You will Fly when your time will Come</h1></marquee>')

def kavi(request):
    return HttpResponse('<h1>Minding your Own Business Shows Respect And Maturity</h1>')