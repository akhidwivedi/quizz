from django.db import models

# Create your models here.
class User(models.Model):
    uname =  models.CharField(max_length = 100)
    option = models.CharField(max_length = 10)
    mul_option = models.CharField(max_length = 10)

    def __str__(self):
        return self.uname
