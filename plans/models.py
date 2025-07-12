from django.db import models


class Subscribe(models.Model):

    """
    This was written under the inspiration of Boutique Ado project code.
    And a student project Fitness-subscription-app
    """

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=254, choices=[
        ('exercise', 'Exercise'),
        ('nutrition', 'Nutrition'),
    ])
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_weeks = models.PositiveIntegerField(default=1)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    level = models.CharField(max_length=20, default=1, choices=[
        ('alpha', 'Alpha'),
        ('beta', 'Beta'),
        ('gamma', 'Gamma'),
    ])

    def __str__(self):
        return self.name
