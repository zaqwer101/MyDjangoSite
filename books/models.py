from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=127)

    def get_books(self):
        return Book.objects.all().filter(author=self)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=127)
    description = models.CharField(max_length=1023)
    id = models.PositiveIntegerField(primary_key=True)

    def __str__(self):
        return self.name
