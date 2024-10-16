from django.db import models


class Post(models.Model):
    head = models.CharField(max_length=30)
    text = models.TextField()
    created_data = models.DateTimeField(auto_now_add=True)

# Create your models here.
