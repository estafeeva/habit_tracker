import os

from django.core.management import BaseCommand

from users.models import User
from dotenv import load_dotenv

load_dotenv()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        if not User.objects.filter(email="admin3@example.com"):
            user = User.objects.create(email="admin3@example.com")
            user.set_password("12345678")

            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.tg = os.getenv("MY_TELEGRAM")
            user.save()
