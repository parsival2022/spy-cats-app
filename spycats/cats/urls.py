from django.urls import path
from .views import *

urlpatterns = [
    path('cat/', CatGetAllCreateView.as_view(), name='cat_get_all_or_create'),     
    path('cat/<int:pk>/', CatGetUpdateDeleteView.as_view(), name='cat_get_update_or_delete'), 
]
