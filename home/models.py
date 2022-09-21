from time import time
from django.db import models

class PostMod(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

# Create your models here.
