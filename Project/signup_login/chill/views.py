from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as user_login,logout as user_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


def default_page(request):
    return render(request,'default.html')

@login_required(login_url='Login')
def home_page(request):
    return render(request,'home.html')

def signup_page(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if User.objects.filter(username=uname):
            messages.error(request,'This username already exists, try another one.')
            return redirect('Signup')
        if User.objects.filter(email=email):
            messages.error(request,'The email already exists, try another one.')
            return redirect('Signup')
        if pass1!=pass2:
            messages.error(request,'The password is incorrect.')
            return redirect('Signup')
        user_obj=User(username=uname,email=email)
        user_obj.set_password(pass1)
        user_obj.save()
        messages.success(request,'Successfully signed in.')
        return redirect('Login')
    return render(request,'signup.html')

def login_page(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        check=User.objects.filter(username=uname)
        if not check:
            messages.error(request,'The username does not exist.')
            return redirect('Login')
        user=authenticate(request,username=uname,password=password)
        if not user:
            messages.error(request,'Invalid login details.')
            return redirect('Login')
        else:
            user_login(request,user)
            messages.success(request,'You have successfully logged in.')
            name=User.objects.get(username=uname).username
            return redirect('Home')
    return render(request,'login.html')

def logout(request):
    user_logout(request)
    messages.success(request,'You have successfully logged out.')
    return redirect('Login')
