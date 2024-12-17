from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, HomePageView, BorrowBookAPIView, ReturnBookAPIView

# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),  # Root URL for the homepage
    path('api/', include(router.urls)),  # API endpoints for books
    path('api/books/<int:pk>/borrow/', BorrowBookAPIView.as_view(), name='borrow-book'),
    path('api/books/<int:pk>/return/', ReturnBookAPIView.as_view(), name='return-book'),
]

