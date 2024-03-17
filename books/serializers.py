from rest_framework import serializers
from .models import Books


class BookSerializer(serializers.ModelSerializer):
    tag_names = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'description',
                  'tag_names']  # Add other fields as needed

    def get_tag_names(self, obj):
        return [tag.name for tag in obj.tags.all()]
