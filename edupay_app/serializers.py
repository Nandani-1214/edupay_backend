from rest_framework import serializers
from .models import Student
from .models import Vendor
from .models import Parent


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    studentRoll = serializers.CharField(source='student.roll')

    class Meta:
        model = Parent
        fields = ['id', 'name', 'email', 'relation', 'address', 'phone', 'studentRoll']
        


