from rest_framework import viewsets, permissions, serializers, status
from rest_framework.response import Response
from django.contrib.auth.models import User

from .models import Books, Loan
from .serializers import BookSerializer, BookLoanSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer


class BookLoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = BookLoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
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

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == status.HTTP_201_CREATED:
            custom_response_data = {'message': 'Book loaned successfully!'}
            return Response(custom_response_data, status=status.HTTP_201_CREATED)

        return response
