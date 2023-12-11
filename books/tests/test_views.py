import pytest
from rest_framework import status


@pytest.mark.django_db
def test_create_a_book(api_client):
    book_data = {
        "title": "My test book", "author": "Author Name", "release_year": 2009
    }

    response = api_client.post(
        "/api/books",
        book_data
    )

    response_json = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert isinstance(response_json.pop("id"), int)
    assert response_json == book_data

@pytest.mark.django_db
def test_create_a_book_title_is_required(api_client):
    book_data = {
        "author": "Author Name", "release_year": 2009
    }

    response = api_client.post(
        "/api/books",
        book_data
    )

    response_json = response.json()

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response_json["title"][0] == "This field is required."

@pytest.mark.django_db
def test_get_a_book(api_client, book_factory):
    book = book_factory()

    response = api_client.get(
        f"/api/books/{book.id}"
    )

    response_json = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_json["title"] == book.title
    assert response_json["author"] == book.author
    assert response_json["release_year"] == int(book.release_year)


@pytest.mark.django_db
def test_get_a_book_not_found(api_client):
    response = api_client.get(
        f"/api/books/1"
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert "Not found" in str(response.json())
