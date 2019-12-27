from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Article, Category, ArticleImage, Comment, Rating


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'required': True, 'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class CategorySerializier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id', 'category_name')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('article_id', 'article_heading', 'article_body', 'image', 'owner', 'category', 'datetime_added')


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ('image_id', 'image', 'article_id')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment_id', 'text', 'article_id', 'author')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('rating_id', 'rate', 'article_id', 'author')