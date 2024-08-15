# from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
# from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
# Create your views here.


class AdCreateAPIView(generics.CreateAPIView):
    """Контроллер создания объявлений"""
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    # permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     """Метод для автоматической привязки объявления к создателю"""
    #     ad = serializer.save()
    #     ad.author = self.request.user
    #     ad.save()


class AdListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка всех объявлений"""
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    # permission_classes = [AllowAny]


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра объявления"""
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    # permission_classes = [IsAuthenticated]


class AdUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для изменения объявления"""
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    # permission_classes = [IsAuthenticated]


class AdDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления объявления"""
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    # permission_classes = [IsAuthenticated]


class MyAdListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка объявлений пользователя"""
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    # permission_classes = [IsAuthenticated]

    # def get_queryset(self):
    #     """Метод для отображение списка объявлений пользователя"""
    #     user = self.request.user
    #     queryset = Ad.objects.filter(author=user)
    #     return queryset


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели отзыва"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    # def get_queryset(self):
    #     """Метод для получения отзывов у определенного объявления"""
    #     ad_id = self.kwargs.get("ad_pk")
    #     ad = get_object_or_404(Ad, id=ad_id)
    #     comment_list = ad.comment_ad.all()
    #     return comment_list.order_by("created_at")

    # def get_permissions(self):
    #     """Создавать и просматривать может любой авторизованный пользователь, а редактировать
    #     и удалять только владелец или админ"""
    #     permission_classes = []
    #     if self.action in ['create', 'list', 'retrieve']:
    #         permission_classes = [IsAuthenticated]
    #         # permission_classes = [AllowAny]
    #     elif self.action in ['update', 'partial_update', 'destroy']:
    #         permission_classes = [IsAdminOrOwner]
    #         # permission_classes = [AllowAny]
    #     return [permission() for permission in permission_classes]

    # def perform_create(self, serializer):
    #     """Метод для автоматической привязки отзыва к создателю у конкретного объявления"""
    #     comment = serializer.save()
    #     comment.author = self.request.user
    #     comment.ad = Ad.objects.get(pk=self.kwargs["ad_pk"])
    #     comment.save()