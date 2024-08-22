from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig

"""
GET "users/djoser/users/" — список профилей пользователей
POST "users/djoser/users/" — регистрация пользователя
GET, PATCH, DELETE "users/djoser/users/{id}/" — в соотвествии с REST и необходимыми permissions (для администратора)
GET PATCH "users/djoser/users/me/" — получение и изменение своего профиля
POST "users/djoser/users/set_password/" — ручка для изменения пароля
POST "users/djoser/users/reset_password/" — ручка для направления ссылки сброса пароля на email
POST users/djoser/"users/reset_password_confirm/" — ручка для сброса своего пароля
POST "users/djoser/token/" — альтернативное получение токена пользователя
POST "users/djoser/token/refresh/" — альтернативное получение рефреш токена пользователя
"""

app_name = UsersConfig.name


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("djoser/", include('djoser.urls'))

]
