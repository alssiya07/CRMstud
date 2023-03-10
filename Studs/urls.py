"""Studs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from details import views

router=DefaultRouter()
router.register("users",views.UsersView,basename="users")
router.register("courses",views.CoursesView,basename="courses")
router.register("batches",views.BatchView,basename="batches")
# router.register("studentprofile",views.CartView,basename="studentprofile")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/',obtain_auth_token)
]+router.urls
