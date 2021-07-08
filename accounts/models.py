from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_lenght=64)
    last_name = models.CharField(max_length=64)
    # username = models.CharField(max_length=128)
    email = models.EmailField(max_length=64, unique=True)
    password = models.CharField(max_length=32)

    # jak stworzyć automatycznie wypełniane pole username z danych name + last_name?
