from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class MyGptApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, default="🍉")
    demoInput = models.TextField(blank=True, null=True)
    propmt = models.TextField(blank=True, null=True)
    usedCount = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(editable=True)

    def __str__(self) -> str:
        return self.user.name
