from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request,'recipes/home.html', context ={
         'name': 'Fábio da Costa',

    })

def contato(request):
    return render(request, 'temp/temp.html')


def sobre(request):
    return HttpResponse('SOBRE')
