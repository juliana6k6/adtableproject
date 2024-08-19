from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.filters import AdFilter
from ads.models import Ad, Comment
from ads.paginators import AdPaginator
from ads.serializers import AdDetailSerializer, AdSerializer, CommentSerializer
from users.permissions import IsAdmin, IsOwner

# Create your views here.


class AdCreateAPIView(generics.CreateAPIView):
    """Контроллер создания объявлений"""

    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод для автоматической привязки объявления к создателю"""
        ad = serializer.save()
        ad.author = self.request.user
        ad.save()


class AdListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка всех объявлений"""

    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    pagination_class = AdPaginator
    permission_classes = [AllowAny]


class AdRetrieveAPIView(generics.RetrieveAPIView):
    """Контроллер для просмотра объявления"""

    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]


class AdUpdateAPIView(generics.UpdateAPIView):
    """Контроллер для изменения объявления"""

    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


class AdDestroyAPIView(generics.DestroyAPIView):
    """Контроллер для удаления объявления"""

    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsAdmin]


class MyAdListAPIView(generics.ListAPIView):
    """Контроллер для просмотра списка объявлений пользователя"""

    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Метод для отображение списка объявлений пользователя"""
        user = self.request.user
        queryset = Ad.objects.filter(author=user)
        return queryset


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для модели отзыва"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """Метод для автоматической привязки отзыва к создателю и к конкретному объявлению"""
        comment = serializer.save()
        comment.author = self.request.user
        comment.ad = Ad.objects.get(pk=self.kwargs["ad_pk"])
        comment.save()

    def get_queryset(self):
        """Метод для получения отзывов у определенного объявления"""
        ad_pk = self.kwargs.get("ad_pk")
        ad = get_object_or_404(Ad, id=ad_pk)
        comment_list = ad.comment_ad.all()
        return comment_list

    # #comment_pk = self.kwargs.get('pk')
    # #serializer.save(author=self.request.user, ad=ad_for_comment, pk=comment_pk)

    def get_permissions(self):
        """Создавать и просматривать может любой авторизованный пользователь, а редактировать
        и удалять только владелец или админ"""
        if self.action in ["create", "list", "retrieve"]:
            permission_classes = IsAuthenticated
            # аутентифицированный пользователь может создавать, просматривать список и или детально один комментарий
        elif self.action in ["update", "partial_update", "destroy"]:
            permission_classes = (IsAuthenticated, IsAdmin | IsOwner)
            # администратор или владелец может отредактировать или удалить
        return super().get_permissions()
