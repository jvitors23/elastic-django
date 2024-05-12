import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


User = get_user_model()


@pytest.fixture(scope="function")
def user() -> User:
    return User.objects.create_user(email="test@email.com", password="test1234", username="teste123")


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    return APIClient()


@pytest.fixture(scope="function")
def authenticated_api_client(api_client: APIClient, user: User) -> APIClient:
    api_client.force_authenticate(user=user)
    return api_client
