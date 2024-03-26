from django.shortcuts import render
from rest_framework import generics, permissions, pagination
from rest_framework.authentication import TokenAuthentication
from .models import Book
from .serializers import BookSerializer

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'isbn'
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
