import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from users.models import User

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv("SUPERUSER_EMAIL"),
            first_name="Test",
            last_name="Testov",
            is_staff=True,
            is_superuser=True,
            is_active=True,
            role="admin",
        )
        user.set_password(os.getenv("SUPERUSER_PASSWORD"))
        user.save()
