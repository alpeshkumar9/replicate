from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Books, Tags, Loan
from .forms import BookLoanAdminForm

User = get_user_model()


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'available')
    list_filter = ('author', 'available',)
    search_fields = ('title', 'author')


class BookLoanAdmin(admin.ModelAdmin):
    form = BookLoanAdminForm
    list_display = ('book', 'reader_full_name',
                    'issue_date', 'due_date')

    def reader_full_name(self, obj):
        return obj.user.get_full_name()
    reader_full_name.short_description = 'Reader'


admin.site.register(Books, BooksAdmin)
admin.site.register(Tags)
admin.site.register(Loan, BookLoanAdmin)
