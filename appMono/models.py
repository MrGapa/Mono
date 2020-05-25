from django.db import models

class TestClass(models.Model):
    user = models.CharField()
    description = models.TextField()
    password = models.CharField()