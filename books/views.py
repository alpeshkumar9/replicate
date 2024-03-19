from rest_framework import viewsets, permissions, serializers, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Books, Loan
from .serializers import BookSerializer, BookLoanSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    Utilizes the BookSerializer to serialize book data.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookLoanViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing book loans.
    Only authenticated users are allowed to create loan records.
    Customizes the creation of loan records to check book availability and user validity.
    """
    queryset = Loan.objects.all()
    serializer_class = BookLoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer: serializers.ModelSerializer) -> None:
        """
        Overrides the default perform_create method to handle book availability
        and user validation before saving a new loan.
        """
        book_instance = serializer.validated_data['book']
        user_id = self.request.data.get('user')

        if not book_instance.available:
            response = {
                'message': 'This book is currently unavailable for loan.'}
            raise serializers.ValidationError(response)

        user = User.objects.get(id=user_id)  # Get the user instance

        if not user:
            raise serializers.ValidationError({'message': 'Invalid user ID.'})

        serializer.save(user=user)

        book_instance.available = False
        book_instance.save()

    def create(self, request, *args, **kwargs) -> Response:
        """
        Overrides the default create method to provide a custom response upon successful book loan creation.
        """
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            custom_response_data = {'message': 'Book loaned successfully!'}
            return Response(custom_response_data, status=status.HTTP_201_CREATED)

        return response
