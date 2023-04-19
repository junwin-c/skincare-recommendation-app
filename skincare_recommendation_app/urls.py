from django.urls import path
from skincare_recommendation_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("", views.home, name="home"),
    path("", views.userHome, name="category")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)