from django.shortcuts import render
from rest_framework.response import Response
from details.serilaizer import RegistrationSerializer,CoursesSerializer,BatchesSerializer,StudentBatchSerilaizer
from details.models import Courses,Batches,BatchStudents
from rest_framework.viewsets import ModelViewSet,ViewSet
from details.models import User
from rest_framework import permissions,authentication
from rest_framework.decorators import action

# -------------------------------------------------
# localhost:8000/users/

class UsersView(ModelViewSet):
    serializer_class=RegistrationSerializer
    queryset=User.objects.all()

# -------------------------------------------------
# courses view

class CoursesView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=CoursesSerializer
    queryset=Courses.objects.all()

# -------------------------------------------------
# listing the courses
# localhost:8000/courses/

    @action(methods=["GET"],detail=True)
    def courses(self,request,*args,**kwargs):  # courses provided
        qs=Courses.objects.values_list("course_name",flat=True).distinct()
        return Response(data=qs)
# --------------------------------------------------
# batch adding
# localhost:8000/courses/1/add_batches/

    @action(methods=["POST"],detail=True)
    def add_batches(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cos=Courses.objects.get(id=id)
        serializer=BatchesSerializer(data=request.data,context={"course":cos})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
# --------------------------------------------------
# list batches by course id
# localhost:8000/courses/1/list_batches/

    @action(methods=["GET"],detail=True)
    def list_batches(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cos=Courses.objects.get(id=id)
        qs=cos.batches_set.all()
        serializer=BatchesSerializer(qs,many=True)
        return Response(data=serializer.data)
# --------------------------------------------------
# listing the batches under each courses

class BatchView(ModelViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=BatchesSerializer
    queryset=Batches.objects.all()

# class StudentBatchView(ModelViewSet):
#     authentication_classes=[authentication.TokenAuthentication]
#     permission_classes=[permissions.IsAuthenticated]
#     serializer_class=BatchesSerializer
#     queryset=BatchStudents.objects.all()

