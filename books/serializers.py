from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowBookSerializer(serializers.Serializer):
    borrower_name = serializers.CharField(max_length=255)
    borrow_date = serializers.DateField()

