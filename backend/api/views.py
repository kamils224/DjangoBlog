import django_filters
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, filters
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from api.serializers import UserSerializer, CommentSerializer, CategorySerializer, RatingSerializer, \
    ArticleImageSerializer
from .models import Article, Comment, Category, Rating, ArticleImage
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrReadOnly, IsAdminUser, IsAdminUserOrReadOnly, IsPostOrIsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsPostOrIsAuthenticated | IsAdminUserOrReadOnly]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly | IsAdminUser]
    filter_backends = [filters.SearchFilter]
    search_fields = ['article_heading']

    def destroy(self, request, *args, **kwargs):
        article = self.get_object()
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleImageViewSet(viewsets.ModelViewSet):
    queryset = ArticleImage.objects.all()
    serializer_class = ArticleImageSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['id', 'article_id']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_fields = ['owner', 'article_id']

    def create(self, request, *args, **kwargs):
        response = super(RatingViewSet, self).create(request, *args, **kwargs)
        self.count_stars(request)
        return response

    def update(self, request, *args, **kwargs):
        response = super(RatingViewSet, self).update(request, *args, **kwargs)
        self.count_stars(request)
        return response

    def count_stars(self, request):
        article = Article.objects.get(id=request.data['article_id'])
        ratings = Rating.objects.filter(article_id=article.id)
        average_ratio = 0.0
        for r in ratings:
            average_ratio += r.rate

        average_ratio = average_ratio / float(len(ratings))
        print(average_ratio)
        article.stars = average_ratio
        article.save()
