from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signin.html', views.sign_in, name='sign_in'),
    path('register.html', views.register, name='register'),
    path('cart.html', views.cart, name='cart'),
]
