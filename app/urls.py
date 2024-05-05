from django.urls import path
from . views import *
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index),
    path("user-login/",sign_in),
    path("courses/",courses),
    path("dashboard/",dashboard),
    path("profile/",profile),
    path("sign-up/",signup),
    path("sign-up-user/",sign_up),
    path("viewstudents/",viewstudents),
    path("course_registration/",course_registration),
    path("add_students/",add_students)
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
