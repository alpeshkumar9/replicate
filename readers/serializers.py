from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Readers
from books.models import Loan


class LoginSerializer(serializers.Serializer):
    """Serializer for user login."""
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(
            username=data['username'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            "Unable to log in with provided credentials.")


class ReadersSerializer(serializers.ModelSerializer):
    """
    Serializer for the Readers model. This class converts the Readers model
    instances into JSON format and vice versa, including all fields defined
    in the model.
    """

    user_full_name = serializers.SerializerMethodField()
    books_on_loan = serializers.SerializerMethodField()

    class Meta:
        model = Readers
        fields = ['id', 'user_id', 'user_full_name', 'library_card_number', 'date_of_birth',
                  'address', 'phone_number', 'membership_start_date', 'books_on_loan']

    def get_user_full_name(self, obj):
        """
        Returns the full name of the user associated with the reader.
        """
        return obj.user.get_full_name()

    def get_books_on_loan(self, obj):
        """
        Returns the titles of all books currently on loan by the reader.
        """
        loans = Loan.objects.filter(user=obj.user).select_related(
            'book')
        return [loan.book.title for loan in loans if loan.book]
