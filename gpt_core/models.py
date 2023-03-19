from django.db import models
from django.db.models.signals import pre_save
from django.contrib.auth import get_user_model

from mygpt.utils import unique_slug_generator

User = get_user_model()


class MyGptApp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, default="🍉")
    demoInput = models.TextField(blank=True, null=True)
    propmt = models.TextField(blank=True, null=True)
    usedCount = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    private = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(editable=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


def product_unique_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_unique_slug_generator, sender=MyGptApp)
