from django.db import models


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
