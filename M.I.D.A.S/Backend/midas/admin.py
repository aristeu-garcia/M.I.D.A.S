from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, Site, Token, Commodity, Strategy, Group

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'username', 'cellphone')
    list_display_links = ('name', 'username')
    search_fields = ('name', 'email', 'username')
    
    def delete_model(self, request, obj):
        super().delete_model(request, obj)


class SiteAdmin(admin.ModelAdmin):
    list_display = ('site', 'client')
    search_fields = ('site',)


class TokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'client')
    search_fields = ('token',)


class CommodityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'client')
    search_fields = ('name', 'code')


class StrategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'commodity', 'client')
    search_fields = ('name',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'admin')
    search_fields = ('name', 'description')


admin.site.register(Client, ClientAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Commodity, CommodityAdmin)
admin.site.register(Strategy, StrategyAdmin)
admin.site.register(Group, GroupAdmin)