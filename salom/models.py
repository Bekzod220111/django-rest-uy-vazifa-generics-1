from django.db import models

# Create your models here.

class Helo(models.Model):
    title = models.CharField(max_length=254)

    def __str__(self):
        return self.title