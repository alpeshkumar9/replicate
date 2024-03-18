import logging
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import LoginSerializer

from .models import Readers
from .serializers import ReadersSerializer


class LoginAPIView(APIView):
    """View to login users."""
    permission_classes = [AllowAny]

    def post(self, request):
        logging.info(request.data)
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "success": True,
                "token": token.key,
                "user": {
                    "first_name": user.first_name,
                    "last_name": user.last_name
                }
            }, status=200)
        else:
            return Response(serializer.errors, status=200)


class VerifyToken(APIView):
    """View to verify tokens."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logging.info(f"Headers: {request.headers}")
        try:
            # `request.auth` contains the token model instance from the header
            # `request.user` contains the user associated with the token
            return Response({
                "success": True,
                "user": {
                    "first_name": request.user.first_name,
                    "last_name": request.user.last_name
                }
            })
        except Token.DoesNotExist:
            raise AuthenticationFailed('Invalid token')


class ReaderViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing book instances.
    """
    queryset = Readers.objects.all()
    serializer_class = ReadersSerializer
