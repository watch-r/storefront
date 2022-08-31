from django.shortcuts import render
from django.http import HttpResponse

def claculate():
    x=1
    y=2
    return x
# Create your views here.
def say_hello(request):
    x=claculate()
    return render(request, 'hello.html',{'name':'Mahmud'})