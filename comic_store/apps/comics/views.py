from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

def index(request):
    return render(request, 'comics/index.html')

def admin(request):
    return render(request, 'comics/admin.html')

def admin_login(request):
    if request.method=="POST":
        admin = User.userManager.admin_login(request.POST)
        if 'errors' in admin:
            for error in admin['errors']:
                messages.error(request, error)
            return redirect('/admin')
        else:
            request.session['id'] = admin['admin'].id
            request.session['auth'] = admin['admin'].admin_auth
            context = {
            "users": User.userManager.all()
            }
            return render(request, 'comics/admin_main.html', context)
    return redirect('/admin')

def register(request):
    if request.method=="POST":
        User.userManager.create(
        email       =   request.POST['email'],
        password    =   request.POST['password'],
        first_name  =   request.POST['first_name'],
        last_name   =   request.POST['last_name'],
        admin_auth  =   request.POST['admin'],
        addr_street =   request.POST['addr_street'],
        street_two  =   request.POST['street_two'],
        addr_city   =   request.POST['addr_city'],
        addr_state  =   request.POST['state'],
        addr_zip    =   request.POST['addr_zip']
        )
    return redirect('/admin')

def product_view(request):
    return render(request, 'comics/admin_products.html')

def orders_view(request):
    return render(request, 'comics/admin_orders.html')
