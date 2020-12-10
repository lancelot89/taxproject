from django.db import models

# Create your models here.


class TaxModel(models.Model):
    annual_income = models.IntegerField()
    insurance_fee = models.IntegerField()
    life_fee = models.IntegerField(blank=True, null=True)
    care_fee = models.IntegerField(blank=True, null=True)
    pension_fee = models.IntegerField(blank=True, null=True)
    blue_yes = models.BooleanField(default=True)
    basic_yes = models.BooleanField(default=True)


class ResultModel(models.Model):
    income_tax = models.IntegerField()
    resident_tax = models.IntegerField()
    health_insurance_tax = models.IntegerField()
    max_housetown_tax = models.IntegerField()
