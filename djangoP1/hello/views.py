from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def laz(request):
    return HttpResponse("Hello, Laz. You're at the polls index.")

def greet(request, name):
    return HttpResponse(f"hello, {name.title()}")

def greet2(request, name):
    return render(request, "hello/greet2.html", {
        "name": name.title()
    })