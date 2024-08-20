from django.contrib import admin

from .models import User


@admin.register(User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "password",
        "phone_number",
        "avatar",
        "role",
        "is_active",
    )
