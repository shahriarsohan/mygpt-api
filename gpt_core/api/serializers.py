from rest_framework import serializers

from gpt_core.models import MyGptApp


class MyGptAppSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyGptApp
        fields = ("__all__")
