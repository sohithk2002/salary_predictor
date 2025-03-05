from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('job-market-insight/', views.job_market_insight, name='job_market_insight'),
    path('skill-gap/', views.skill_gap, name='skill_gap'),
]
