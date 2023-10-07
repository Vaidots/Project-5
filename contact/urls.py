from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactMessage, name='contact'),
    path('team-members/', views.team_member_list, name='team_member_list'),
    path('team/<int:pk>/', views.team_member_detail, name='team_detail'),
]
