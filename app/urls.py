from django.urls import path
from . views import *
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index),
    path("user-login/",sign_in),
    path("courses/",courses),
    path("delete/<int:pk>/",delete_course,name='delete'),
    path("update_course/",update_course),
    path("updatecourse/<int:uid>/",updatecourse, name="updatecourse"),
    path("update_student/",update_student),
    path("updatestudent/<int:uid>/",updatestudent, name="updatestudent"),
    path("delete_student/<int:pk>/",delete_student, name='delete_student'),
    path("dashboard/",dashboard),
    path("profile/<int:pk>/",profile ,name='profile'),
    path("sign-up/",signup),
    path("sign-up-user/",sign_up),
    path("viewstudents/",viewstudents),
    path("course_registration/",course_registration),
    path("add_students/",add_students),
    path("student_profile/<int:pk>/", student_profile, name="student_profile"),
    path("search/",search,name='search'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
