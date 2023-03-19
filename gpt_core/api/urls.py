from django.urls import path

from .views import TestNewGptAPP, CreateNewGptAPP, MyAppToPerform

urlpatterns = [
    path("", CreateNewGptAPP.as_view()),
    path("test", TestNewGptAPP.as_view()),
    path("use/<slug>", MyAppToPerform.as_view())
]
