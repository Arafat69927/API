from rest_framework import serializers
from my_app.models import *

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentModel
        fields = '__all__'

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subjectModel
        fields = '__all__'