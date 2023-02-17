from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def hello_view(request):
#     return HttpResponse("hello world!")


def index(request):
    return render(request, 'index.html')


def signin(request):
    return render(request, 'signin.html')


def register(request):
    return render(request, 'register.html')


def cart(request):
    return render(request, 'cart.html')


def product_detail(request):
    return render(request, 'product-detail.html')


def store(request):
    return render(request, 'store.html')
