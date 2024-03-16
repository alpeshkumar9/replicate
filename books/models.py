from django.db import models


class Books(models.Model):
    """
    Represents a book in the library, including details about its title,
    author, ISBN, publication date, and availability.
    """
    title: str = models.CharField(max_length=255)
    author: str = models.CharField(max_length=255)
    isbn: str = models.CharField(max_length=13, unique=True)
    publication_date: models.DateField = models.DateField()
    available: bool = models.BooleanField(default=True)

    def __str__(self) -> str:
        """Return the book's title as its string representation."""
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
