from rest_framework import serializers
from django.contrib.auth.models import User
from details.models import Courses, Batches,Students,BatchStudents


class RegistrationSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta():
        model=User
        fields=["id","first_name","last_name","username","password","email"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
#---------------------------------------------------------------------------------------
class BatchesSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    course=serializers.CharField(read_only=True)
    batch_code=serializers.CharField()
    started_date=serializers.CharField(read_only=True)
    is_active=serializers.BooleanField(read_only=True)

    class Meta():
        model=Batches
        fields=["id","course","batch_code","started_date","is_active"]

    def create(self,validated_data):
        course=self.context.get("course")
        return Batches.objects.create(**validated_data,course=course)

# ------------------------------------------------------------------------------------
class CoursesSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    course_batches=BatchesSerializer(read_only=True,many=True)

    class Meta():
        model=Courses
        fields=["id","course_name","fees","duration","is_active","course_batches"]

# --------------------------------------------------------------------------------------
class StudentBatchSerilaizer(serializers.ModelSerializer):
    class Meta():
        model=BatchStudents
        fields=["id","student","batch"]

    def create(self, validated_data):
        user=self.context.get("user")
        batch=self.context.get("batch")
        return Batches.objects.create(user=user,batch=batch,**validated_data)

class StudentSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta():
        model=Students
        fields=["id","user","dob","resume","qualification"]