from django.db import models

# Create your models here.


class Content(models.Model):
    url = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    date_updated = models.DateTimeField(null=False, auto_now=True)
    date_created = models.DateTimeField(null=False, auto_now_add=True)
