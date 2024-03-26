# restapi/tests.py
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.book = Book.objects.create(
            title='Test Book',
            authors='Test Author',
            isbn='1234567890123'
        )

    def test_list_books(self):
        url = reverse('book-list-create')  # Updated URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_book(self):
        data = {
            'title': 'New Book',
            'authors': 'New Author',
            'isbn': '9876543210987'
        }
        url = reverse('book-list-create')  # Updated URL name
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'isbn': self.book.isbn})  # Updated URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        data = {
            'title': 'Updated Book',
            'authors': 'Updated Author',
            'isbn': self.book.isbn
        }
        url = reverse('book-detail', kwargs={'isbn': self.book.isbn})  # Updated URL name
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'isbn': self.book.isbn})  # Updated URL name
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
