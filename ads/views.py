from django.shortcuts import render
from rest_framework import generics
# Create your views here.


class AdCreateAPIView(generics.CreateAPIView):
    """Контроллер создания объявлений"""
    serializer_class = AdDetailSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Метод для автоматической привязки объявления к создателю"""
        serializer.save(author=self.request.user)