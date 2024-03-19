from typing import Any
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db.models import Model

from .models import Books, Tags, Loan
from .forms import BookLoanAdminForm

User = get_user_model()


class BooksAdmin(admin.ModelAdmin):
    """
    Admin view for Books model.
    """
    list_display = ('title', 'author', 'publication_date', 'available')
    list_filter = ('author', 'available',)
    search_fields = ('title', 'author')


class BookLoanAdmin(admin.ModelAdmin):
    """
    Admin view for Loan model, specifically for managing book loans.
    """
    form = BookLoanAdminForm
    list_display = ('book', 'reader_full_name', 'issue_date', 'due_date')

    def reader_full_name(self, obj: Model) -> str:
        """
        Returns the full name of the user who has loaned a book.

        :param obj: Loan model instance.
        :return: Full name of the user.
        """
        return obj.user.get_full_name()
    reader_full_name.short_description = 'Reader'


admin.site.register(Books, BooksAdmin)
admin.site.register(Tags)
admin.site.register(Loan, BookLoanAdmin)
