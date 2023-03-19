from rest_framework import views, response, status, permissions
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView

from .serializers import AccountsSerializer


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FetchUser(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        serializer = AccountsSerializer(request.user)
        return response.Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        api_key = request.data.get("api_key")
        user.license_key = api_key
        user.save()
        return response.Response({"msg": "Api Key updated successfully"}, status=status.HTTP_200_OK)
