from django.urls import path
from .views import LoginAPIView, VerifyToken

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token-verify/', VerifyToken.as_view()),
]
