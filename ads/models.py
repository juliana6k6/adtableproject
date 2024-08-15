from django.db import models
from django.utils import timezone
from users.models import User


class Ad(models.Model):
    """Модель объявления должна содержать следующие поля:
   - title — название товара;
   - price — цена товара (целое число);
   - description — описание товара;
   - author — пользователь, который создал объявление;
   - created_at — время и дата создания объявления.
   Объявления должны быть отсортированы по дате создания (чем новее, тем выше).
    """

    title = models.CharField(max_length=150,
                             verbose_name="название товара", help_text="Укажите название товара"
                             )
    price = models.PositiveIntegerField(
        default=0, verbose_name="цена товара", help_text="Укажите цену товара"
    )
    description = models.TextField(max_length=400, default='нет описания товара',
                                   verbose_name="описание товара", help_text="Введите описание товара")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ad_author',
        blank=True,
        null=True,
        verbose_name="Автор",
        help_text="Автор объявления",
        )
    image = models.ImageField(upload_to="ads/", verbose_name="фото товара", help_text="Загрузите фото товара",
                              blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="дата и время создания", blank=True, null=True)


    def __str__(self):
        return f"{self.title} - {self.price}"

    class Meta:
        verbose_name = "объявление"
        verbose_name_plural = "объявления"
       # ordering = ('-created_at',)


class Comment(models.Model):
    """Модель отзыва должна содержать следующие поля:
   - text — текст отзыва;
   - author — пользователь, который оставил отзыв;
   - ad — объявление, под которым оставлен отзыв;
   - created_at — время и дата создания отзыва.
   """

    text = models.TextField(max_length=400, verbose_name="текст отзыва", help_text="Введите текст отзыва")
    author = models.ForeignKey(
        User, related_name='comment_author',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Автор отзыва",
    )
    ad = models.ForeignKey(Ad, related_name='comment_ad', on_delete=models.CASCADE,
                           verbose_name='объявление, под которым оставлен отзыв', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now, verbose_name="дата и время создания", null=True, blank=True)


    def __str__(self):
        return f"Отзыв от {self.created_at} написан {self.author}"

    class Meta:
        verbose_name = "отзыв"
        verbose_name_plural = "отзывы"
       # ordering = ('-created_at',)
