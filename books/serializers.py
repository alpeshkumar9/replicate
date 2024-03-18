from rest_framework import serializers

from .models import Books, Loan


class BookSerializer(serializers.ModelSerializer):
    tag_names = serializers.SerializerMethodField()

    class Meta:
        model = Books
        fields = ['id', 'title', 'author', 'description',
                  'tag_names', 'available']

    def get_tag_names(self, obj):
        return [tag.name for tag in obj.tags.all()]


class BookLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ['id', 'user', 'book',
                  'issue_date']
