from rest_framework import serializers
from .models import Books


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.
    """

    class Meta:
        model = Books
        fields = '__all__'
