from rest_framework import serializers
from.models import *

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'