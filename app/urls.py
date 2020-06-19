from django.urls import path, include
from app import views

urlpatterns = [
	path('ping/', views.task)
]