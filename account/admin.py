from django.contrib import admin

from .models import User

def marquer_comme_staff(modeladmin, request, queryset):
    queryset.update(is_staff=True)
    
marquer_comme_staff.short_description = "Marquer comme staff"

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'adresse', 'is_staff', 'is_superuser')
    list_filter = ('is_staff',)    
    search_fields = ('email', 'first_name', 'last_name')
    actions = [marquer_comme_staff]

admin.site.register(User, UserAdmin)