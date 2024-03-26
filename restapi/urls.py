from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('api/books/<str:isbn>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]