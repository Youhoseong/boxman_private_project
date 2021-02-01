






from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from users import views as user_views


app_name="users"

urlpatterns = [
   path("", user_views.HomeView.as_view(), name="home")
]
