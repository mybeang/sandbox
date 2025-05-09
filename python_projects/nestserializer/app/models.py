from django.db import models

# Create your models here.

class BillingModel(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    account_id = models.CharField(max_length=36)
    invoice_month = models.CharField(max_length=15)
    product_name = models.CharField(max_length=100)
    service_name = models.CharField(max_length=100)
    usage_date = models.DateTimeField()
    usage_amount = models.FloatField(default=0)
    cost = models.FloatField(default=0)
    cost_discount = models.FloatField(default=0)
    credit_discount = models.FloatField(default=0)

    class Meta:
        db_table = 'tb_billing'


class ChargeCodeModel(models.Model):
    account_id = models.CharField(max_length=36)
    charge_code = models.CharField(max_length=16)

    class Meta:
        db_table = 'tb_charge_code'


class CurrencyModel(models.Model):
    currency = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        db_table = 'tb_currency'

