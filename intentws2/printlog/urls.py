from django.urls import path
from . import views

urlpatterns = [
    path('', views.print_view, name='print'),
    path('label/', views.print_label_view, name='print_label'),
    path('boxlabel/', views.print_boxlabel_view, name='print_boxlabel'),
    path('extraboxlabel/', views.print_extraboxlabel_view, name='print_extraboxlabel'),
]