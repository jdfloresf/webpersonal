from django.shortcuts import render
from .models import Project
from django.views.generic import ListView, DetailView


# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name = "core/templates/core/portfolio.html"
    context_object_name = 'proyectos'
    ordering = ['-created']


class ProjectDetailView(DetailView):
    model = Project
    template_name = "core/templates/core/project_detail.html"
    context_object_name = 'proyecto'

