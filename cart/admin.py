# cart/admin.py

from django.contrib import admin
from .models import Delivery, Facture, Facture_Articles

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('delivery_system', 'prix')
    search_fields = ('delivery_system',)
    ordering = ('delivery_system',)

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ('date_emission', 'id_delivery', 'total_htc', 'client_id')
    list_filter = ('date_emission', 'id_delivery', 'client_id')
    search_fields = ('client_id__username',)
    ordering = ('date_emission',)

@admin.register(Facture_Articles)
class FactureArticlesAdmin(admin.ModelAdmin):
    list_display = ('facture_id', 'article_id', 'quantity')
    list_filter = ('facture_id',)
    search_fields = ('article_id__nom',)
    ordering = ('facture_id',)
