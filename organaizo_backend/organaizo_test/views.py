from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def calculate():
    x=1
    y=2
    return x
def say_hello(request):
    #Pull data from db
    # Transform
    # send email
    x = calculate()
    return HttpResponse('Hello World')