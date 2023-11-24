from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        email = form.get('email')
        pass1 = form.get('password1')
        pass2 = form.get('password2')
        if not username or not email or not pass1 or not pass2:
            messages.error(request, "Incomplete details")
            return render(request, "account/signup.html")
        if pass1 != pass2:
            messages.error(request, "Password does not match!!!")
            return render(request, "account/signup.html")
        if len(pass1) < 8:
            messages.error(request, "Password less than 8 character")
            return render(request, "account/signup.html")
        if User.objects.filter(username = username).exists():
            messages.error(request, "Username already taken")
            return render(request, "account/signup.html")
        if User.objects.filter(email = email).exists():
            messages.error(request, "Email already taken")
            return render(request, "account/signup.html")
        user = User.objects.create(username=username, email=email)
        user.set_password(pass1)
        user.save()
        messages.success(request, "Sign up successful")
        return redirect('login')
    return render(request, "account/signup.html")


def login(request):
    if request.method == 'POST':
        form = request.POST
        username = form.get('username')
        pass1 = form.get('password')
        if not username or not pass1:
            messages.error(request, "Incomplete details")
            return render(request, "account/login.html")
        user = auth.authenticate(username = username, password = pass1)
        if not user:
            username_exist = User.objects.filter(email = username)
            if not username_exist:
                messages.error(request, "Incorrect login details")
                return render(request, "account/login.html")
            user_username = User.objects.get(email = username)
            user = auth.authenticate(username = user_username.username, password = pass1)
            if not user:
                messages.error(request, "Incorrect login details")
                return render(request, "account/login.html")
            
        auth.login(request, user)
        messages.success(request, "Login successful")
        return redirect(reverse('product:home'))
    return render(request, "account/login.html")

def logout(request):
    auth.logout(request)
    return redirect(reverse('product:home'))
