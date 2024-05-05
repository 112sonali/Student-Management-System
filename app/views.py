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
    course_obj = Course.objects.all()
    return render(request,"courses.html", {"course_obj":course_obj})

def course_registration(request):
    if request.method =="POST":
        course_name=request.POST["course_name"]
        fees=request.POST["fees"]
        duration=request.POST["duration"]
        if Course.objects.filter(course_name=course_name).exists():
            return HttpResponse("Cousre name already existS")
        else:
            Course.objects.create(course_name=course_name,fees=fees,duration=duration)
            return redirect('/courses/')


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
    course_obj = Course.objects.all()
    student_obj = Student.objects.all()
    return render(request,"viewstudents.html",{"course_obj":course_obj ,"student_obj":student_obj})
    
   
    

def add_students(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile_no = request.POST.get("mobile_no")
        college = request.POST.get("college")
        degree = request.POST.get("degree")
        address = request.POST.get("address")
        image = request.FILES.get("image")
        course_id = request.POST.get("courses")
        new_course = Course.objects.get(id=course_id)
        print(new_course)
        if Student.objects.filter(email=email).exists():
            return HttpResponse("email already exist")
        elif Student.objects.filter(mobile_no=mobile_no).exists():
            return HttpResponse("mobile_no already exist")
        else:
            stu = Student.objects.create(name=name,email=email,mobile_no=mobile_no, 
                                        college=college,degree=degree,
                                        address=address,image=image,
                                        courses=new_course)
            print(stu)                            
            return redirect("/viewstudents/")
        


        








