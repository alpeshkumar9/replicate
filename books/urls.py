from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookLoanViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'book/loan', BookLoanViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
