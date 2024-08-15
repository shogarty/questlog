from django.contrib import admin
from Tenants.models import Tenant, TenantAwareModel, Quest

from Tenants.utils import tenant_from_request

# Register your models here.
from .models import Character

admin.site.register(Character)
admin.site.register(Quest)
admin.site.register(Tenant)
