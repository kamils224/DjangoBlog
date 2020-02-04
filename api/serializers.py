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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name')


class ArticleSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs['owner'] = self.context['request'].user
        return attrs

    class Meta:
        model = Article
        fields = ('id', 'article_heading', 'article_body', 'image', 'owner', 'category', 'datetime_added')
        read_only_fields = ['owner']


class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        fields = ('id', 'image', 'article_id')


class CommentSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs['owner'] = self.context['request'].user
        return attrs

    class Meta:
        model = Comment
        fields = ('id', 'text', 'article_id', 'owner')


class RatingSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        attrs['owner'] = self.context['request'].user
        return attrs

    class Meta:
        model = Rating
        fields = ('id', 'rate', 'article_id', 'owner')
