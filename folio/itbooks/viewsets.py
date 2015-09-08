from .serializers import BookSerializer, GetBookSerializer
from .models import Book, GetBook
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class BookViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class GetBookViewset(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = GetBook.objects.all()
    serializer_class = GetBookSerializer