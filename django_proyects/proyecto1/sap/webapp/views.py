from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenidos(request):
    return HttpResponse("Bienvenidos a SAP")