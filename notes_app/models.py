from django.db import models


class Note(models.Model):
    notes = models.CharField(max_length=300)


# Create your models here.
