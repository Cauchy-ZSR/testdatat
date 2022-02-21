from django.db import models

# Create your models here.


class demo(models.Model):
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=2)

    class Meta:
        db_table = "userInfo"