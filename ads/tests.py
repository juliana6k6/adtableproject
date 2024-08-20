from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ads.models import Ad
from users.models import User


class AdViewSetsTestCase(APITestCase):

    def setUp(self) -> None:

        # Создание тестового пользователя
        self.user = User.objects.create(email='testov@test.ru', password='12345')
        # Аутентификация пользователя
        self.client.force_authenticate(user=self.user)
        # Создание тестовое объявление
        self.ad = Ad.objects.create(title='test ad', author=self.user, price=10,
                                    description='test description')

    def test_ad_create(self):
        """Тестирование создания привычки"""
        url = reverse("ads:ad-create")
        data = {
            "title": "test ad2",
            "author": self.user.pk,
            "price": 5,
            "description": "test description",
        }
        response = self.client.post(url, data)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        ad = Ad.objects.get(title='test ad2')
        author = self.user
        self.assertEqual(author, ad.author)
        self.assertEqual(Ad.objects.all().count(), 2)

    def test_retrieve_ad(self):
        """Тестирование просмотра информации об объявлении"""
        url = reverse('ads:ad-detail', args=[self.ad.pk])
        response = self.client.get(url)
        data = response.json()
        print(data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("price"), self.ad.price)

    def test_update_ad(self):
        """Тестирование редактирования объявления"""
        url = reverse('ads:ad-update', args=[self.ad.pk])
        data = {
            'title': 'update test ad2',
            'description': 'test description2'
        }
        response = self.client.put(url, data)
        data1 = response.json()
        print(data1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.ad.refresh_from_db()
        self.assertEqual(self.ad.title, 'update test ad2')

    def test_delete_ad(self):
        """Тестирование удаления объявления"""
        url = reverse('ads:ad-delete', args=[self.ad.pk])
        response = self.client.delete(url)
        print(f"{self.ad.title} удалено")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Ad.objects.all().count(), 0)
        self.assertFalse(Ad.objects.filter(id=self.ad.id).exists())