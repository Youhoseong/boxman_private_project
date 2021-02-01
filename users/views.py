from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User

from django.views.generic import ListView
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class HomeView(ListView):
    model = User
    template_name = "home.html"
    context_object_name = "USER"
