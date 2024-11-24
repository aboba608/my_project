from rest_framework import viewsets
from .models import News, Category, Tag
from .serializers import NewsSerializer, CategorySerializer, TagSerializer
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-publication_date')
    serializer_class = NewsSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'tags']
    search_fields = ['title', 'content']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


from django.shortcuts import render
from .models import News


def news_list_view(request):
    news_list = News.objects.order_by('-publication_date')
    return render(request, 'news_list.html', {'news_list': news_list})


