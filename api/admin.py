from django.contrib import admin
from .models import Book


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year_published', 'review')