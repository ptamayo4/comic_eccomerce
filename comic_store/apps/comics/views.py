from django.shortcuts import render

def index(request):
    return render(request, 'comics/index.html')

def admin(request):
    return render(request, 'comics/admin.html')
