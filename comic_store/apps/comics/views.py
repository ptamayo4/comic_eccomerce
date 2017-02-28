from django.shortcuts import render

def index(request):
    return render(request, 'comics/index.html')

def products_main(request):
    return render(request, 'comics/products_main.html')

def product_spotlight(request):
    return render(request, 'comics/product_spotlight.html')

def shopping_cart(request):
    return render(request, 'comics/shopping_cart.html')
