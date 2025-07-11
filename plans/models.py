from django.db import models


class Subscribe(models.Model):

    """
    This was written under the inspiration of Boutique Ado project code.
    And a student project Fitness-subscription-app
    """
    
    category = models.CharField(max_length=254, choices=[
        ('exercise', 'Exercise'),
        ('nutrition', 'Nutrition'),
    ])
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    charge = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    subscription_duration = models.PositiveIntegerField(default=1)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    stages = models.CharField(max_length=20, choices=[
        ('alpha', 'Beginner'),
        ('beta', 'Intermediate'),
        ('gamma', 'Advanced'),
    ])

    def __str__(self):
        return self.name
