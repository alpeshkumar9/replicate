from django.contrib import admin
from .models import Books


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publication_date', 'available')
    list_filter = ('author', 'available',)
    search_fields = ('title', 'author', 'isbn')


admin.site.register(Books, BooksAdmin)
