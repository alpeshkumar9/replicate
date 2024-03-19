from rest_framework import serializers
from .models import Books, Loan


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Books model.
    Includes a method field for getting tag names associated with a book.
    """
    tag_names = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = ['id', 'title', 'author',
                  'description', 'tag_names', 'available']

    def get_tag_names(self, obj) -> list:
        """
        Retrieves a list of tag names associated with the book.
        """
        return [tag.name for tag in obj.tags.all()]


class BookLoanSerializer(serializers.ModelSerializer):
    """
    Serializer for the Loan model.
    """
    class Meta:
        model = Loan
        fields = ['id', 'user', 'book', 'issue_date']
