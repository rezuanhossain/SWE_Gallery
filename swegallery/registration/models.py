from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    batch = models.IntegerField()
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.userid