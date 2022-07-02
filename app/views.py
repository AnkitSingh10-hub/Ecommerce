from django.shortcuts import render, redirect
from .models import Slider, Banner, Category, SubCategory, MainCategory, Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def BASE(request):
    return render(request, 'base.html')


def HOME(request):
    sliders = Slider.objects.all().order_by('-id')[0:3]
    banners = Banner.objects.all().order_by('-id')[0:3]
    maincategory = MainCategory.objects.all().order_by('-id')
    product = Product.objects.filter(section__name="Top Deal of the Day")
    context = {
        'sliders': sliders,
        'banners': banners,
        'maincategory': maincategory,
        'product': product,
    }
    return render(request, 'Main/home.html', context)


def track(request):
    return render(request, 'order-tracking.html')


def PRODUCT_DETAILS(request, slug):
    product = Product.objects.filter(slug=slug)
    if product.exists():
        product = Product.objects.get(slug=slug)
    else:
        return redirect('404')
    context = {
        'product': product,
    }

    return render(request, 'product/product_detail.html', context)


def Error404(request):
    return render(request, 'errors/404.html')


def MY_ACCOUNT(request):
    return render(request, 'account/my-account.html')


def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username = username).exists():
            messages.error(request, 'username already exists')
            return redirect('my_account')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'email id already exists')
            return redirect('my_account')
        user = User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()
        return redirect('my_account')
    return render(request, 'account/my-account.html')


def LOGIN(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Email and Password are Invalid !')
            return redirect('my_account')
    return render(request, 'account/my-account.html')
