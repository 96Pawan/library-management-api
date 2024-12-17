from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book
from rest_framework.views import APIView
from .serializers import BookSerializer, BorrowBookSerializer
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

class HomePageView(APIView):
    def get(self, request):
        return Response({"message": "Welcome to the Library Management API"})

class BookPagination(PageNumberPagination):
    page_size = 5  
    page_size_query_param = 'page_size'  
    max_page_size = 100  

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing books.
    Includes endpoints for listing, adding, and searching books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination  # Apply pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['genre', 'author']  # Enable filtering by genre and author
    search_fields = ['title', 'author']  # Enable searching by title and author


class BorrowBookAPIView(GenericAPIView):
    """
    API endpoint to borrow a book.
    Request body requires:
    - borrower_name (string)
    - borrow_date (date)
    """
    serializer_class = BorrowBookSerializer

    def get(self, request, pk):
        """Render the form for borrowing a book."""
        serializer = self.get_serializer()
        return Response(serializer.data)

    def post(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        if book.is_borrowed:
            return Response({"error": "Book is already borrowed."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            book.is_borrowed = True
            book.borrower_name = serializer.validated_data['borrower_name']
            book.borrow_date = serializer.validated_data['borrow_date']
            book.save()
            return Response(
                {"success": f"Book '{book.title}' has been borrowed successfully."},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReturnBookSerializer(serializers.Serializer):
    """Empty serializer for returning a book."""
    pass

class ReturnBookAPIView(GenericAPIView):
    """
    API endpoint to return a borrowed book.
    No request body is required.
    """
    serializer_class = ReturnBookSerializer

    def get(self, request, pk):
        """Render the form for returning a book."""
        serializer = self.get_serializer()
        return Response(serializer.data)

    def post(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"error": "Book not found."}, status=status.HTTP_404_NOT_FOUND)

        if not book.is_borrowed:
            return Response({"error": "Book is not currently borrowed."}, status=status.HTTP_400_BAD_REQUEST)

        # Reset book status
        book.is_borrowed = False
        book.borrower_name = None
        book.borrow_date = None
        book.save()

        return Response(
            {"success": f"Book '{book.title}' has been returned successfully."},
            status=status.HTTP_200_OK
        )
        
