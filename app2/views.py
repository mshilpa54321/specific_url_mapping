from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Virat(request):
    return HttpResponse('Virat is best batsman')

def ABD(request):
    return HttpResponse('He is a monster')
