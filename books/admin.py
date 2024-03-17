from django.contrib import admin
from .models import Books, Tags


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'available')
    list_filter = ('author', 'available',)
    search_fields = ('title', 'author')


admin.site.register(Books, BooksAdmin)
admin.site.register(Tags)
