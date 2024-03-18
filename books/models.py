from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    """
    Represents a book in the library, including details about its title,
    author, ISBN, publication date, and availability.
    """
    title: str = models.CharField(max_length=255)
    author: str = models.CharField(max_length=255)
    tags = models.ManyToManyField(
        'Tags', related_name='book_tags', blank=True)
    description: str = models.TextField(blank=True, null=True)
    publication_date: models.DateField = models.DateField(
        blank=True, null=True)
    available: bool = models.BooleanField(default=True)

    def __str__(self) -> str:
        """Return the book's title as its string representation."""
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Tags(models.Model):
    """
    Represents a genre of books in the library.
    """
    tag_id: int = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        """Return the genre's name as its string representation."""
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Loan(models.Model):
    """
    Represents a record of a book being loaned out to a reader from the library.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='book_reader')
    book = models.ForeignKey(
        'Books', on_delete=models.CASCADE, related_name='book_loaned')
    issue_date = models.DateField(auto_now_add=True, verbose_name="Issue Date")
    due_date = models.DateField(verbose_name="Due Date", blank=True, null=True)

    def __str__(self) -> str:
        return f"'{self.book.title}' loaned to {self.user.get_full_name()} on {self.issue_date}"

    def save(self, *args, **kwargs):
        if not self.id:
            issue_date = timezone.now().date()
            self.due_date = issue_date + timedelta(days=30)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Book Loan"
        verbose_name_plural = "Book Loans"
