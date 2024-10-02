from django.urls import path
from .views import *


app_name = 'portfolio_app'

urlpatterns = [
    path('', ProjectListView.as_view(), name='portfolio'),
    path('project-detail/<pk>/', ProjectDetailView.as_view(), name='portfolio_detail')
]
