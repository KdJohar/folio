from .models import GetBook, Book
from rest_framework import serializers

class GetBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetBook


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
