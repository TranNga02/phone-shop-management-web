from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logoutPage, name='logout'),
    path('search.html', views.search, name='search'),
]
