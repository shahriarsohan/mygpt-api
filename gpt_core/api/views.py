
import openai
from rest_framework import views, generics, permissions, response, status

from gpt_core.models import MyGptApp
from .serializers import MyGptAppSerializers

# TODO Test endpoint will not use for now. This endpoint will use to test the app before create


class TestNewGptAPP(views.APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def post(self, request, *args, **kwargs):
        user = request.user
        openai.api_key = user.license_key

        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            temperature=0.7,
            presence_penalty=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            messages=[
                {"role": "user", "content": request.data.get(
                    "prompt") + " " + request.data.get("example_input"), }
            ]
        )

        if 'choices' in res:
            if len(res['choices']) > 0:
                answer = res['choices'][0]['message']['content']
            else:
                answer = 'Opps sorry, you beat the AI this time'
        else:
            answer = 'Opps sorry, you beat the AI this time'

        return response.Response({
            "msg": "Hey I am working correctly",
            "payload": answer
        }, status=status.HTTP_200_OK)


class CreateNewGptAPP(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        user = request.user
        qs = MyGptApp.objects.select_related(
            "user").filter(user=user).order_by("-id")
        serializer = MyGptAppSerializers(qs, many=True)
        return response.Response({
            "payload": serializer.data
        })

    def post(self, request, *args, **kwargs):
        user = request.user
        request.data['user'] = user.id
        serializer = MyGptAppSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({
                "msg": "App created successfully",
                "payload": serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return response.Response({
                "msg": "Something went wrong when creating app for you",
                "error": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


class MyAppToPerform(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        slug = self.kwargs["slug"]
        obj = MyGptApp.objects.select_related("user").filter(slug=slug).first()
        if obj:
            serializer = MyGptAppSerializers(obj)
            return response.Response({
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        else:
            return response.Response({
                "error": "App not found"
            }, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        slug = self.kwargs["slug"]
        app_obj = MyGptApp.objects.select_related(
            "user").filter(slug=slug).first()
        try:
            app_obj.usedCount += 1
            app_obj.save()
        except:
            pass
        openai.api_key = app_obj.user.license_key

        res = openai.ChatCompletion.create(
            model="text-davinci-003",
            temperature=0.7,
            presence_penalty=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            messages=[
                {"role": "user", "content": app_obj.propmt +
                    " " + request.data.get("msg"), }
            ],
            stop=["\n"]
        )
        if 'choices' in res:
            if len(res['choices']) > 0:
                answer = res['choices'][0]['message']['content']
            else:
                return response.Response({"err": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({"err": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
        return response.Response({"answer": answer})


class Test(views.APIView):
    def get(self, request, *args, **kwargs):
        return response.Response({"msg": "DONE!"})
