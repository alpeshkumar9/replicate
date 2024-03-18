from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LoginAPIView, VerifyToken

from .views import ReaderViewSet

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token-verify/', VerifyToken.as_view()),
]

router = DefaultRouter()
router.register(r'', ReaderViewSet)

urlpatterns += [
    path('', include(router.urls)),
]
