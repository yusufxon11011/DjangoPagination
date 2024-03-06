from django.shortcuts import render

from django.http import HttpResponse

def first(request):
    return HttpResponse("<h1>You are in the first page.</h1>")

def second(request):
    return HttpResponse("<h1>You are in the second page.</h1>")

def third(request):
    return HttpResponse("<h1>You are in the third page.</h1>")

def fourth(request):
    return HttpResponse("<h1>You are in the fourth page.</h1>")

def last(request):
    return HttpResponse("<h1>You are in the last page.</h1>")