from django.db import models

# Create your models here.
class TestClass(models.Model):
    user = models.CharField()
    description = models.TextField()