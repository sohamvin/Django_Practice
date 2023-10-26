from django.http import HttpResponse
from django.shortcuts import render





def Home(request,*args, **kwargs):

        return HttpResponse("<h1> Hello World </h1>")

def About(request,*args, **kwargs):

        return HttpResponse("<h1> About Section </h1>")

def Link(request,*args, **kwargs):
        print(request)
        print(args)
        print(kwargs)
        return HttpResponse("<h1> Link </h1>")




# Create your views here.

