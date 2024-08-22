from django.urls import include, path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig

"""
GET "api/users/djoser/users/" — список профилей пользователей
POST "api/users/djoser/users/" — регистрация пользователя
GET, PATCH, DELETE "api/users/djoser/users/{id}/" — в соотвествии с REST и необходимыми permissions (для администратора)
GET PATCH "api/users/djoser/users/me/" — получение и изменение своего профиля
POST "api/users/djoser/users/set_password/" — ручка для изменения пароля
POST "api/users/djoser/users/reset_password/" — ручка для направления ссылки сброса пароля на email
POST api/users/djoser/users/reset_password_confirm/" — ручка для сброса своего пароля
POST "api/users/djoser/token/" — альтернативное получение токена пользователя
POST "api/users/djoser/token/refresh/" — альтернативное получение рефреш токена пользователя
"""

app_name = UsersConfig.name


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("djoser/", include('djoser.urls'))

]
