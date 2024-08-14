from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="SUPERUSER_EMAIL", first_name="Test", last_name="Testov",
            is_staff=True, is_superuser=True, is_active=True,
        )
        user.set_password("SUPERUSER_PASSWORD")
        user.save()
