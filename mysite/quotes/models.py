from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return f'"{self.text[:30]}..." - {self.author}'

class Tag(models.Model):
    name = models.CharField(max_length=50)
    quotes = models.ManyToManyField(Quote, related_name='tags')

    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
