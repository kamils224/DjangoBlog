from django.contrib import admin
from .models import Article, Category, Comment, Rating, ArticleImage


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(ArticleImage)