from django.contrib import admin

from .models import Review, Comment, Title, Genre, Category


admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Title)
admin.site.register(Genre)
admin.site.register(Category)
