from django.db import models


class Menu(models.Model):
    """Menu model."""
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    parent = models.ForeignKey(
        'self', null=True,
        blank=True, on_delete=models.CASCADE,
        related_name='children',
    )

    class Meta:
        ordering = ['name', 'parent__id', 'id']

    def __str__(self):
        return self.name
