from django.urls import path
from . import views

urlpatterns = [
    path('create_scrap_record/', views.create_scrap_record_view, name='create_scrap_record'),
    path('manager/', views.manager_view, name='manager'),
    path('remove_scrap_record/', views.remove_scrap_record_view, name='remove_scrap_record'),
]