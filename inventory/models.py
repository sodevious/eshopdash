from django.db import models
from django.conf import settings
from marketplaces.models import Marketplace

# this needs to be an app
INVENTORY_CATEGORY_CHOICES = [
    ('clothing', 'Clothing'),
    ('shoes', 'Shoes')
]

class Item(models.Model):
    name = models.CharField(max_length=200, default='', null=True, blank=True)
    meta = models.CharField(max_length=200, default='', null=True, blank=True)
    purchase_date = models.DateField('Date item was purchased', null=True, blank=True)
    purchase_price = models.FloatField(help_text="include sales tax if any", null=True, blank=True)
    purchased_marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, help_text='average per item')
    weight = models.FloatField(null=True, blank=True)
    category = models.CharField(
        max_length=24,
        choices=INVENTORY_CATEGORY_CHOICES,
        default='',
        null=True,
        blank=True
    )
    condition = models.CharField(
        max_length=24,
        choices=settings.CONDITION_CHOICES,
        default='new',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

class Expense(models.Model):
    purchase_date = models.DateField('Date item was purchased', null=True, blank=True)
    purchase_price = models.FloatField('Date item was sold', null=True, blank=True)
    purchased_marketplace = models.ForeignKey(Marketplace, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    # category

#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
