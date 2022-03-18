from django.db import models

# Create your models here.

class grade(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
class demo(models.Model):
    name = models.CharField(max_length=32)
    age = models.CharField(max_length=2)
    grade = models.ForeignKey(grade, on_delete=models.CASCADE)
    time = models.DateField()
    class Meta:
        db_table = "userInfo"