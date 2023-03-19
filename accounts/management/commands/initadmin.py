import environ

from django.conf import settings
from django.core.management.base import BaseCommand
from accounts.models import Accounts

env = environ.Env()


class Command(BaseCommand):

    def handle(self, *args, **options):
        if Accounts.objects.count() == 0:
            for user in settings.ADMINS:
                admin = Accounts.objects.create_superuser(
                    email="admin@test.com", password="minda54321")
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
