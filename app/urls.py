from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('base/', views.BASE, name='base'),
    path('', views.HOME, name='home'),
    path('track/', views.track, name='track'),
    path('product/<slug:slug>', views.PRODUCT_DETAILS, name='product_detail'),
    path('404/', views.Error404, name='404'),
    path('account/myaccount/', views.MY_ACCOUNT, name='my_account'),
    path('account/register/', views.REGISTER, name='register'),
    path('account/login/', views.LOGIN, name='login'),
]
