from django.contrib import admin
from Tenants.models import Tenant, TenantAwareModel

from Tenants.utils import tenant_from_request

# Register your models here.
from .models import Game, Character, Quest


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    fields = ["name", "owner"]

    def get_queryset(self, request, *args, **kwargs):
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        queryset = queryset.filter(tenant=tenant)
        return queryset

    def save_model(self, request, obj, form, change):
        tenant = tenant_from_request(request)
        obj.tenant = tenant
        super().save_model(request, obj, form, change)

admin.site.register(Character)
admin.site.register(Quest)
admin.site.register(Tenant)
