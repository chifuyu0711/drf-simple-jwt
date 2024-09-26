from rest_framework import generics, permissions, serializers
from django.contrib.auth.models import User
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated


# Фильтр для модели Blog
class BlogFilter(filters.FilterSet):
    tags = filters.CharFilter(field_name='tags__name', lookup_expr='exact')

    class Meta:
        model = Blog
        fields = ['tags']


# Сериализатор для профиля пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


# Список и создание блогов
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = BlogFilter  # Используйте ваш кастомный фильтр
    search_fields = ['title', 'body']
    ordering_fields = ['created_at', 'title']


# Детальная информация о блоге
class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Комментарии
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]


# Профиль пользователя
class UserProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# My Blog (CRUD для авторизованных пользователей)
class MyBlogView(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)
