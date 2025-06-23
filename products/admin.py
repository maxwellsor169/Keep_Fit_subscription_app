from django.contrib import admin
from .models import Product, Category

"""
This Tells admin which field to display
This Register Product model in admin panel
"""


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)
    search_fields = ['name', 'description', 'sku']
    list_filter = ('category', 'status', 'price')


"""
This Register Category model in admin panel
This Adds how category items are displaying.
"""


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)