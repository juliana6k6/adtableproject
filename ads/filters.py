import django_filters

from ads.models import Ad


class AdFilter(django_filters.rest_framework.FilterSet):
    """Класс для фильтрации объявлений по названию"""

    title = django_filters.CharFilter(
        field_name="title",
        lookup_expr="icontains",
    )

    # CharFilter — специальный фильтр, который позволяет искать совпадения в текстовых полях модели
    # icontains: Нечувствительное к регистру содержание подстроки
    class Meta:
        model = Ad
        fields = ("title",)
