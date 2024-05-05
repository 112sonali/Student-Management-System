from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=250)

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    fees = models.IntegerField()
    duration = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField( max_length=200)
    email = models.EmailField(max_length=250)
    mobile_no = models.IntegerField()
    college = models.CharField(max_length=290)
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    degree = models.CharField(max_length=200)
    address = models.TextField()
    image = models.FileField(upload_to='profile', max_length=100 )



