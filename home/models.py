from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=122)
    queries = models.TextField(max_length=150)
    date = models.DateField()

    def __str__(self):
        return self.name
