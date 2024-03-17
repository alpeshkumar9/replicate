from django.db import models


class Books(models.Model):
    """
    Represents a book in the library, including details about its title,
    author, ISBN, publication date, and availability.
    """
    title: str = models.CharField(max_length=255)
    author: str = models.CharField(max_length=255)
    categories = models.ManyToManyField(
        'Category', related_name='book_category', blank=True)
    genres = models.ManyToManyField(
        'Genre', related_name='book_genre', blank=True)
    descriptiom: str = models.CharField(max_length=255, blank=True, null=True)
    publication_date: models.DateField = models.DateField(
        blank=True, null=True)
    available: bool = models.BooleanField(default=True)

    def __str__(self) -> str:
        """Return the book's title as its string representation."""
        return self.title

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"


class Category(models.Model):
    """
    Represents a category for books in the library. A book can belong to multiple
    categories, and a category can contain multiple books.
    """
    category_id: int = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        """
        Return the category's name as its string representation.
        """
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Genre(models.Model):
    """
    Represents a genre of books in the library.
    """
    genre_id: int = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        """Return the genre's name as its string representation."""
        return self.name
