from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    category_name = models.CharField(max_length=32)

    def __str__(self):
        return self.category_name


class Article(models.Model):
    article_heading = models.CharField(max_length=20)
    article_body = models.TextField(max_length=10000)
    image = models.ImageField(blank=True, default='default.jpg')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    datetime_added = models.DateTimeField(auto_now_add=True, blank=True)
    stars = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        output_size = (300, 300)
        img.thumbnail(output_size)
        img.save(self.image.path)

    def __str__(self):
        return self.article_heading


class ArticleImage(models.Model):
    image = models.ImageField()
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=250)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    datetime_added = models.DateTimeField(auto_now_add=True, blank=True)


class Rating(models.Model):
    rate = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super.save(Rating,*args, **kwargs)