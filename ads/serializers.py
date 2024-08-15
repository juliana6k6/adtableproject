from rest_framework import serializers
from ads.models import Ad, Comment


class AdSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели объявления"""

    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'description', 'image', 'created_at')


class CommentSerializer(serializers.ModelSerializer):
    """Базовый сериализатор для модели отзыва"""

    class Meta:
        model = Comment
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детального просмотра одного объявления"""

    # comment = CommentSerializer(source='comment_ad', read_only=True, many=True)

    class Meta:
        model = Ad
        fields = '__all__'
