import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from books.tests.factories import BookFactory

register(BookFactory)


@pytest.fixture
def api_client():
    return APIClient()