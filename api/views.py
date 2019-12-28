import django_filters
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from api.serializers import UserSerializer, CommentSerializer, CategorySerializier, RatingSerializer, \
    ArticleImageSerializer
from .models import Article, Comment, Category, Rating, ArticleImage
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminUser, IsAdminUserOrReadOnly


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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def destroy(self, request, *args, **kwargs):
        article = self.get_object()
        article.delete()
        return Response('Article was deleted')


class ArticleImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage
    serializer_class = ArticleImageSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class CommentViewSet(viewsets.ModelViewSet):
    http_method_names = ['post', 'delete', 'put']
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
