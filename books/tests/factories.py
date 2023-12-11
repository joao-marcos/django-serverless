import factory

from books.models import Book

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = factory.Faker("sentence", nb_words=5)
    author = factory.Faker("name")
    release_year = factory.Faker("year")
