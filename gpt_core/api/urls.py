from django.urls import path

from .views import TestNewGptAPP

urlpatterns = [
    path("test", TestNewGptAPP.as_view())
]
