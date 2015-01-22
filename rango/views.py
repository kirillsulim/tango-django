from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hi! I''m ducking work! <br/><a href = "./about/">About</a>')

def about(request):
    return HttpResponse('Hi! It''s ducking about! <br/><a href = "../">Go home</a>')
