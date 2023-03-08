from django.urls import path
from skincare_recommendation_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("category", views.category, name="category")
]