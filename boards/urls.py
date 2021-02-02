from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from boards import views as board_views

app_name="boards"

urlpatterns = [
   path("", board_views.HomeView.as_view(), name="home")
]
