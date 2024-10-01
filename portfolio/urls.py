from django.urls import path
from .views import *


app_name = 'portfolio_app'

urlpatterns = [
    path('portfolio/', ProjectListView.as_view(), name='portfolio'),
    path('portfolio/<int:pk>/', ProjectDetailView.as_view(), name='portfolio_detail')
]
