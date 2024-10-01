from django.urls import path

from . import views    

app_name = 'core_app'

urlpatterns = [
    path('home/', views.home, name="home"),
    path('about-me/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
]