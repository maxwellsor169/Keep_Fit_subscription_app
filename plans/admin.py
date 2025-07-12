from django.contrib import admin
from .models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'level',
        'category',
        'price',
        'rating',
        'image',
        'duration_weeks',
    )

    ordering = ('level',)
    search_fields = ['name', 'description',]
    list_filter = ('category', 'level', 'price')
    

admin.site.register(Subscribe, SubscribeAdmin)    

