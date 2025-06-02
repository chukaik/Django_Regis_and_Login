from django.shortcuts import render, redirect
from .models import myUsers
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.http import HttpResponse

# Create your views here.

@never_cache  # Prevent caching of this view
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('registerPage')  # Redirect to registerPage if already logged in
    if request.method == 'POST':
        if 'login' in request.POST:
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('registerPage')
            else:
                messages.error(request, "Invalid email or password.")

    return render(request, 'base/loginPage.html')


@login_required(login_url='loginPage')

@never_cache  # Prevent caching of this view
def registerPage(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            
            name = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            myuser = myUsers.objects.filter(email=email)

            if myuser.exists():
                messages.error(request, "User already exists with this email.")
            
            else:
                myuser = myUsers.objects.create_user(
                    name=name,
                    email=email,
                    password=password
                )
                myuser.set_password(password)  # Ensure password is hashed
                myuser.save()
                return HttpResponse('User Added successfully! <a href="/registerPage" style="color:blue; text-decoration:underline;">Add Another User</a>')  # Placeholder response
            
    return render(request, 'base/registerPage.html')

def logouts(request):
    logout(request)
    return redirect('loginPage')