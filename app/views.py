from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def index(request):
    return render(request,"index.html")

def sign_in(request):
    if request.method == "POST":
        person=user.objects.get(email=request.POST['email'])
        if check_password(request.POST['password'],person.password):
            request.session['index']=True
            request.session['email']=person.email
            return redirect('/dashboard/')
        else:
            return HttpResponse('Invalid email and password')


def courses(request):
    return render(request,"courses.html")

def dashboard(request):
    return render(request,"dashboard.html")

def profile(request):
    return render(request,"profile.html")

def signup(request):
    return render(request,"sign-up.html")

def sign_up(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        password=make_password(request.POST["password"])
        if user.objects.filter(email=email).exists():
            return HttpResponse("Email already exist")
        else:
            user.objects.create(name=name,email=email,password=password)
            return redirect('/')

def viewstudents(request):
    return render(request,"viewstudents.html")







