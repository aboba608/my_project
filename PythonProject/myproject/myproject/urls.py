from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news import views

router = DefaultRouter()
router.register(r'news', views.NewsViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'tags', views.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
