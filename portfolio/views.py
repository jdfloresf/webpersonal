from django.shortcuts import render
from .models import Project
from django.views.generic import ListView, DetailView


# Create your views here.

app_name = 'portfolio_app'

class ProjectListView(ListView):
    model = Project
    template_name = "portfolio/project_list.html"
    context_object_name = 'proyectos'
    ordering = ['-created']


class ProjectDetailView(DetailView):
    model = Project
    template_name = "portfolio/project_detail.html"
    context_object_name = 'proyecto'

