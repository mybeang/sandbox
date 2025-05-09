from django.contrib import admin
from app.models import ChargeCodeModel, CurrencyModel


# Register your models here.
class ChargeCodeAdmin(admin.ModelAdmin):
    fields = ['account_id', 'charge_code']
    list_display = ['account_id', 'charge_code']


class CurrencyAdmin(admin.ModelAdmin):
    fields = ['currency', 'start_date', 'end_date']
    list_display = ['currency', 'start_date', 'end_date']


admin.site.register(ChargeCodeModel, ChargeCodeAdmin)
admin.site.register(CurrencyModel, CurrencyAdmin)
