from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsOwner(BasePermission):
    """Класс для проверки принадлежности продукта владельцу"""

    message = "Доступно владельцу"

    # разрешение на уровне объекта
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False


class IsAdmin(BasePermission):
    """Класс для проверки роли администратора"""

    message = "Доступно администраторам."

    # разрешение на уровне пользователя
    def has_permission(self, request, view):
        return request.user.role == UserRoles.ADMIN
