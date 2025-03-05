from django.urls import path
from .views import home, job_market_insight, skill_gap

urlpatterns = [
    path('', home, name='home'),
    path('job-market-insight/', job_market_insight, name='job_market_insight'),
    path('skill-gap/', skill_gap, name='skill_gap'),
]