from django.contrib import admin

from .models import ContractType, Order

admin.site.register(Order)
admin.site.register(ContractType)
