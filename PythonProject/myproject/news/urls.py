from django.urls import path, include
from .views import news_list_view

urlpatterns = [
    path('', include('news.urls')),  # Связывает маршруты приложения "news" с корнем проекта
]
