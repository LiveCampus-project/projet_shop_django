from django.contrib import admin

from .models import Facture, Delivery


class FactureAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'total_htc', 'id_delivery', 'date_emission')
    list_filter = ('client_id',)    
    search_fields = ('client_id',)

admin.site.register(Facture, FactureAdmin)

class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('delivery_system', 'prix')    
    search_fields = ('delivery_system',)

admin.site.register(Delivery, DeliveryAdmin)
