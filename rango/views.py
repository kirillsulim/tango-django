from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = \
        {'boldmessage': "I'm ducking bold!",
         }

    return render(request, 'rango/index.html', context_dict)

def about(request):
    return  render(request, 'rango/about.html')
