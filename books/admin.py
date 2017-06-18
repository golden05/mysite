from django.contrib import admin
from .models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_field = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'authors', 'publisher')
    filter_horizontal = ('authors',)

admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
