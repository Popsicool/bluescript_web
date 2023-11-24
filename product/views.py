from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, "product/index.html")

def product_creation(request):
    if not request.user.is_authenticated:
        return redirect(reverse('product:home'))
    user = request.user
    if not user.is_staff:
        return redirect(reverse('product:home'))
    
    if request.method == 'POST':
        form = request.POST
        name = form.get('name')
        name = form.get('name')
        name = form.get('name')
        name = form.get('name')
        name = form.get('name')
        name = form.get('name')
    
    return render(request, 'product/create.html')