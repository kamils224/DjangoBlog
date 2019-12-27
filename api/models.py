from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name


class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=32)
    article_body = models.TextField(max_length=256)
    image = models.ImageField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    datetime_added = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.article_heading


class ArticleImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    image = models.ImageField()
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=250)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Rating(models.Model):
    rating_id = models.AutoField(primary_key=True)
    rate = models.FloatField
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
