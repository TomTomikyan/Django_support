from django.db import models

# Create your models here.

class support(models.Model):

    email = models.EmailField('email')
    text = models.TextField('text')

    def __str__(self) -> str:
        return self.email