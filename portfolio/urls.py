from django.urls import path
from .views import *


app_name = 'portfolio_app'

urlpatterns = [
    path('', ProjectListView.as_view(), name='portfolio'),
    path('blog-detail/<slug>/', ProjectDetailView.as_view(), name='blog_detail')
]
