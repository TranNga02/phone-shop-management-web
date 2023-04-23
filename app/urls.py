from django.urls import path
from . import views
urlpatterns = [
    # path('',views.index,name="index"),
    path('', views.home, name='home'),
    path('signin.html', views.sign_in, name='sign_in'),
    path('register.html', views.register, name='register'),
    path('cart.html', views.cart, name='cart'),
]
