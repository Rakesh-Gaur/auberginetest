from django.db import models

# Create your models here.
class Imageurl(models.Model):
    image_url = models.CharField(max_length=2000)
    compress_url = models.CharField(max_length=2000)
