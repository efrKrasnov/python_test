from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')