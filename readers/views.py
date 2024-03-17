import logging
from django.contrib.auth import login
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import LoginSerializer


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
            return Response(serializer.errors, status=400)
