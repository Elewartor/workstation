from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.create_unit_view, name='create_unit'),
]