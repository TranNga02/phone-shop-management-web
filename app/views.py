from django.shortcuts import get_object_or_404, render,redirect
from django.http import JsonResponse
from .models import *
import json
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.db.models import Sum
from django.core.paginator import Paginator


def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
        paginator = Paginator(keys, 9)
        page = request.GET.get('page')
        product_list = paginator.get_page(page)
    categories = Category.objects.all()
    return render(request, 'app/search.html',{"searched":searched,"keys":keys,'product_list':product_list,"categories":categories})

def home(request):
    if request.user.is_authenticated:
        order_items = OrderItem.objects.filter(order__customer=request.user, order__complete=False)
        total_items = order_items.aggregate(Sum('quantity'))['quantity__sum']
        total_items = int(total_items)
    else:
        total_items = 0
    categories = Category.objects.all()
    total_products = Product.objects.count()
    products = Product.objects.all()
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    context = {'products' : products,'total_products':total_products,'categories':categories,'total_items' : total_items,'product_list':product_list}
    return render(request, 'app/home.html',context)

def navbar(request):
    if request.user.is_authenticated:
        order_items = OrderItem.objects.filter(order__customer=request.user, order__complete=False)
        total_items = order_items.aggregate(Sum('quantity'))['quantity__sum']
        total_items = int(total_items)
    else:
        total_items = 0
    return render(request, 'app/includes/navbar.html',{'total_items':total_items})

def logoutPage(request):
    logout(request)
    return redirect('sign_in')

