from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=32)
    age = models.IntegerField(default=18)
    bio = models.TextField(max_length=300)
    email = models.EmailField()
    proffession = models.CharField(max_length=80)

    def __str__(self):
        return self.name