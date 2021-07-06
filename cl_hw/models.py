from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)
    born_info = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        ordering = ['id']
        verbose_name = 'Author'

    def __str__(self):
        return self.name


class Quotes(models.Model):
    quotes = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
        verbose_name = 'Quotes'

    def __str__(self):
        return self.quotes
