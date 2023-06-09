from django.urls import path, re_path

from .views import (
    FacebookLogin,
    GoogleLogin,
    FetchUser
)

urlpatterns = [
    re_path(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    re_path(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),
    path('user', FetchUser.as_view(), name="fetch-user")
]
