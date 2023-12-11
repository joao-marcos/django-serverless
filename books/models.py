from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    release_year = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.id} - {self.title}"
