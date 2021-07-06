from django.contrib import admin

from .models import Author, Quotes


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'born_info', 'description', 'id')


@admin.register(Quotes)
class QuotesModelAdmin(admin.ModelAdmin):
    list_display = ['quotes', 'author', 'id']
