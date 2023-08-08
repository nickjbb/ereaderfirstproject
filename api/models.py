from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, help_text="Enter genres")

    def __str__(self):
        return self.name

class PDF(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text="What is the document's genre?")

    def __str__(self):
        return self.title


class Author(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

