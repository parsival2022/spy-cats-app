from django.urls import path
from .views import *

urlpatterns = [
    path('mission/', MissionGetAllCreateView.as_view(), name='mission_get_all_or_create'),     
    path('mission/<int:pk>/', MissionGetUpdateDeleteView.as_view(), name='mission_get_update_or_delete'), 
    path('target/<int:pk>/', TargetGetUpdateView.as_view(), name='target_get_or_update'), 
]
