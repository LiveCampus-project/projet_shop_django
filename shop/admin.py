from django.contrib import admin

from .models import Articles, Categories


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description', 'prix', 'stock', 'categorie_id')
    list_filter = ('categorie_id',)    
    search_fields = ('nom', 'categorie_id')

admin.site.register(Articles, ArticleAdmin)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)    
    search_fields = ('nom',)

admin.site.register(Categories, CategorieAdmin)