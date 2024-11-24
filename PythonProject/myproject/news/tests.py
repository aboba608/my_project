from rest_framework.test import APITestCase
from .models import News, Category, Tag

class NewsAPITest(APITestCase):
    def setUp(self):
        # Создание тестовых данных
        pass

    def test_get_news_list(self):
        response = self.client.get('/api/news/')
        self.assertEqual(response.status_code, 200)
