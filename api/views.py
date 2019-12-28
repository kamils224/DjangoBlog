import django_filters
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from api.serializers import UserSerializer, CommentSerializer, CategorySerializier, RatingSerializer, \
    ArticleImageSerializer
from .models import Article, Comment, Category, Rating, ArticleImage
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializier
    permission_classes = [IsAdminUser]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class ArticleImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage
    serializer_class = ArticleImageSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
