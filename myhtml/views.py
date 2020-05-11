from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>hello Anish<h1>")
def check(request):
    return render(request,"txt.html")
def next(request):
    return render(request,"frame.html")
