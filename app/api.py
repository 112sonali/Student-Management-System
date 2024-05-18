from .models import *
from rest_framework import generics
from .serializer import Userserializer


class Userapi(generics.CreateAPIView):
    queryset = user.objects.all()
    serializer_class = Userserializer

class updateapi(generics.RetrieveUpdateAPIView):
    queryset = user.objects.all()
    serializer_class = Userserializer

class deleteapi(generics.DestroyAPIView):
    queryset = user.objects.all()
    serializer_class = Userserializer
