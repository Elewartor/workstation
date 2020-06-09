from django.urls import path
from . import views

urlpatterns = [
    path('', views.print_view, name='print'),
    path('boxlabel/', views.print_boxlabel_view, name='print_boxlabel'),
]