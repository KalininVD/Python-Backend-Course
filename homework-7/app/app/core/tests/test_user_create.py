import pytest
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db
class TestUserCreate:
    def test_create_user(self, client):
        url = reverse('user-list')
        data = {
            "username": "new_user",
            "email": "new_user@example.com",
            "password": "password123",
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['username'] == "new_user"

    def test_create_user_unauthorized(self, client):
        url = reverse('user-list')
        data = {
            "username": "unauthorized_user",
            "email": "unauthorized_user@example.com",
            "password": "password123",
            "is_superuser": True,
            "is_staff": True,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_create_user_with_existing_username(self, client, user):
        url = reverse('user-list')
        data = {
            "username": user.username,
            "email": "new_user@example.com",
            "password": "password123",
            "is_superuser": False,
            "is_staff": False,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'username' in response.data

    def test_create_user_with_invalid_email(self, client):
        url = reverse('user-list')
        data = {
            "username": "new_user",
            "email": "invalid_email",
            "password": "password123",
            "is_superuser": False,
            "is_staff": False,
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'email' in response.data

    def test_create_user_with_missing_fields(self, client):
        url = reverse('user-list')
        data = {
            "username": "new_user",
            "password": "password123",
        }
        response = client.post(url, data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'email' in response.data