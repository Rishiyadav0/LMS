from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')
    isbn = models.CharField(max_length=20, unique=True)

    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()

    def __str__(self):
        return self.title