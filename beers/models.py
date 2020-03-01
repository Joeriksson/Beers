from django.db import models


class Beer(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=200)
    first_brewed = models.CharField(max_length=20)
    description = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Beer: {self.name}'
