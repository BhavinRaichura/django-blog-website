from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from blog.forms import NewClient
from datetime import date

from blog.models import *
# Create your views here.

def home(response):
    dataset={'title':'Home'}
    return render(response,'base.html',dataset)

    

def create_ac(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('tel')
        password = request.POST.get('password')
        create_user= Clients(username=username,email=email,phone_number=phone_number,password=password)
        create_user.save()
        return redirect('home')
    return render(request, 'register.html', {})


def user_logout(request):
    logout(request)
    return redirect('home')


def profile(response):
    return HttpResponse("<h1>profile</h1>")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        db=Clients.objects
        if db.filter(username=username,password=password):
            user = authenticate(username=username, password=password)
            print(user)
            if user is not None:
               login(request, user)
               return redirect('home')
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields') 
    return render(request, 'login.html', {})

   

def new_blog(response):
    if request.method=='POST':
        blogtitle=request.POST.get("blogtitle")
        blogbody=request.POST.get("blogbody")
        blogimg=request.POST.get("blogimg")
        blogtime=date.today()
        blogid=0
    return HttpResponse("<h1>new blog</h1>")

def blogs(response):
    return HttpResponse("<h1>blogs/h1>")

def forget_password(response):
    return HttpResponse("<h1>forget password</h1>")

def blog_search(response,keywords):
    return HttpResponse("<h1>ablog search</h1>")

