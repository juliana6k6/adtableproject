# from rest_framework import generics
# from users.models import User
# from users.serializers import UserRegistrationSerializer
#
#
# class UserCreateAPIView(generics.CreateAPIView):
#     """Эндпоинт создания пользователя"""
#
#     serializer_class = UserRegistrationSerializer
#     queryset = User.objects.all()
#     # permission_classes = [AllowAny]
#
#     def perform_create(self, serializer):
#         user = serializer.save(is_active=True)  # сделали пользователя активным
#         user.set_password(user.password)  # хешируется пароль
#         user.save()
