from django.contrib import admin
from Tenants.models import Tenant, TenantAwareModel, Quest, Character

from Tenants.utils import tenant_from_request

# Register your models here.

admin.site.register(Character)
admin.site.register(Quest)
admin.site.register(Tenant)
