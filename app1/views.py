from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def Dhoni(request):
    return HttpResponse('MSD is a best finisher')


def Raina(request):
    return HttpResponse('Raina is known as MR.IPL')
