from django.shortcuts import render
from django.views.generic import ListView
from . import models
# Create your views here.

class HomeView(ListView):
    model = models.Board
    template_name = "index.html"
    context_object_name = "BOARD"