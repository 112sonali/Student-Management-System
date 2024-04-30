from django.urls import path
from . views import *

urlpatterns = [
    path("",index),
    path("user-login/",sign_in),
    path("courses/",courses),
    path("dashboard/",dashboard),
    path("profile/",profile),
    path("sign-up/",signup),
    path("sign-up-user/",sign_up),
    path("viewstudents/",viewstudents)
]
