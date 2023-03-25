from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf.urls.static import static
from django.views.generic import TemplateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('accounts.api.urls')),
    path('api/core/', include('gpt_core.api.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
