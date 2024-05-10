from django.shortcuts import render,redirect
from . models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request,"index.html")

def sign_in(request):
    if request.method == "POST":
        person=user.objects.get(email=request.POST['email'])
        print(person)
        if check_password(request.POST['password'],person.password):
            request.session['index']=True
            request.session['email']=person.email
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Invalid email and password')
            return redirect('/')


def courses(request):
    course_obj = Course.objects.all()
    return render(request,"courses.html", {"course_obj":course_obj})

def course_registration(request):
    if request.method =="POST":
        course_name=request.POST["course_name"]
        fees=request.POST["fees"]
        duration=request.POST["duration"]
        if Course.objects.filter(course_name=course_name).exists():
            messages.error(request, "Cousre name already existS")
        else:
            Course.objects.create(course_name=course_name,fees=fees,duration=duration)
            return redirect('/courses/')
        
def delete_course(request,pk):
    Course.objects.get(id=pk).delete()
    return redirect('/courses/')

def updatecourse(request,uid):
    update_obj=Course.objects.get(id=uid)
    return render(request, "update-course.html", {"update_obj":update_obj})

def update_course(request):
    if request.method =="POST":
        uid = request.POST["uid"]
        course_name=request.POST["course_name"]
        fees=request.POST["fees"]
        duration=request.POST["duration"]
        Course.objects.filter(id=uid).update(course_name=course_name,fees=fees,duration=duration)
        messages.success(request,"User Update Sucessfully")
        return redirect('/courses/')
        

def dashboard(request):
    return render(request,"dashboard.html")

def profile(request,pk):
    student_obj = Student.objects.get(id=pk)
    return render(request,"profile.html" , {"student_obj":student_obj})

def signup(request):
    return render(request,"sign-up.html")

def sign_up(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        password=make_password(request.POST["password"])
        if user.objects.filter(email=email).exists():
            messages.error(request, "Email already exist")
            return redirect('/sign-up/')
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
            messages.error(request , "email already exist")
        elif Student.objects.filter(mobile_no=mobile_no).exists():
            messages.error(request , "mobile_no already exist")
        else:
            stu = Student.objects.create(name=name,email=email,mobile_no=mobile_no, 
                                        college=college,degree=degree,
                                        address=address,image=image,
                                        courses=new_course)
            messages.success(request, "student add successfully")                         
            return redirect("/viewstudents/")
        
def delete_student(request,pk):
    Student.objects.get(id=pk).delete()
    return redirect('/viewstudents/')
        
def updatestudent(request,uid):
    course_obj = Course.objects.all()
    update_obj=Student.objects.get(id=uid)
    return render(request, "update-student.html", {"course_obj":course_obj, "update_obj":update_obj})

def update_student(request):
    if request.method =="POST":
        uid = request.POST.get("uid")
        name = request.POST.get("name")
        email = request.POST.get("email")
        mobile_no = request.POST.get("mobile_no")
        college = request.POST.get("college")
        degree = request.POST.get("degree")
        address = request.POST.get("address")
        image = request.FILES.get("image")
        course_id = request.POST.get("courses")
        new_course = Course.objects.get(id=course_id)
        Student.objects.filter(id=uid).update(name=name, email=email, mobile_no=mobile_no, college=college
                                             ,degree=degree, address=address, image=image, courses=new_course)
        messages.success(request,"student Update Sucessfully")
        return redirect('/viewstudents/')
    
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(name__icontains=q) | Q(email__icontains=q)) | Q(mobile_no__icontains=q)
        student_obj = Student.objects.filter(multiple_q)
        print(multiple_q)
    else:
        student_obj = Student.objects.all()
    context = {'student_obj':student_obj}
    return render(request,'viewstudents.html',context)

        

def student_profile(request,pk):
    Student.objects.get(id=pk)
    return redirect("/profile/")
        


        








