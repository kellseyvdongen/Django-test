from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import ToDoItem


class AllToDos(ListView):
    model = ToDoItem
    template_name = "todo/index.html"