from django.shortcuts import render
from .models import *
def home(request):
    products = Product.objects.all()
    context = {'products' : products}
    return render(request, 'app/home.html',context)

def sign_in(request):
    return render(request, 'app/account/sign_in.html')

def register(request):
    return render(request, 'app/account/register.html')

def cart(request):
    # if request.user.is_authenticated:
    # customer = request.user.customer
    # order,created = Order.objects.get_or_create(customer = customer , complete = False)
    # items = order.orderitem_set.all()
    # # else:
    # #     items = []
    order = Order.objects.all()
    items = OrderItem.objects.all()
    context = {'items':items,'order':order}
    return render(request, 'app/order/cart.html',context)