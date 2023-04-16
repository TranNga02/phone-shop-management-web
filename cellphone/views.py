from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def sign_in(request):
    return render(request, 'account/sign_in.html')

def register(request):
    return render(request, 'account/register.html')

def cart(request):
    return render(request, 'order/cart.html')