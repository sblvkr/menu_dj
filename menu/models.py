from django.db import models


class Menu(models.Model):
    """Menu model."""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)
