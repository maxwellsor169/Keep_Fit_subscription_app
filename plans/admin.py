from django.contrib import admin
from .models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'stages',
        'category',
        'charge',
        'rating',
        'image',
        'subscription_duration',
    )

    ordering = ('stages',)
    search_fields = ['name', 'description',]
    list_filter = ('category', 'stages', 'charge')
    

admin.site.register(Subscribe, SubscribeAdmin)    

