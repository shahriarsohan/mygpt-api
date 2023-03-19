from rest_framework import serializers

from accounts.models import Accounts


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = [
            "email",
            "username",
            "license_key"
        ]
