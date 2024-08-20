from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig

# from users.views import UserCreateAPIView
"""
GET "users/" — список профилей пользователей
POST "users/" — регистрация пользователя
GET, PATCH, DELETE "users/{id}" — в соотвествии с REST и необходимыми permissions (для администратора)
GET PATCH "users/me" — получение и изменение своего профиля
POST "users/set_password" — ручка для изменения пароля
POST "users/reset_password" — ручка для направления ссылки сброса пароля на email*
POST "users/reset_password_confirm" — ручка для сброса своего пароля*
"""
users_router = SimpleRouter()
app_name = UsersConfig.name

users_router.register("users", UserViewSet, basename="users")
urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # path("register/", UserCreateAPIView.as_view(), name="user_register"),
    path("", include(users_router.urls)),
    # по умолчанию path("api/", include('djoser.urls'))
    # обратите внимание, что здесь в роутере мы регистрируем ViewSet,
    # который импортирован из приложения Djoser
]
