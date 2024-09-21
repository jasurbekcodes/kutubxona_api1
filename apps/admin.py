from django.contrib import admin

from apps.models import Author, Genre, Book


admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
