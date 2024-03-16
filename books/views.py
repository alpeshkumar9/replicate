from rest_framework import viewsets
from .models import Books
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Books.objects.all()
    serializer_class = BookSerializer
