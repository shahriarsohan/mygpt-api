
import openai
from rest_framework import views, generics, permissions, response

from gpt_core.models import MyGptApp


class TestNewGptAPP(views.APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        user = request.user
        openai.api_key = user.license_key

        res = openai.Completion.create(
            model="text-davinci-003",
            prompt="",
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,

        )
        print(res)
        return response.Response(res)


class CreateNewGptAPP(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
