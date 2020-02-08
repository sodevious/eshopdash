from django.db import models
from inventory.models import Item
from django.conf import settings

LOCATION_CHOICES = [
    ('domestic', 'Domestic'),
    ('inernational', 'International')
]

SHIPPING_TYPES = [
    ('first_class', 'USPS First Class'),
    ('priority', 'USPS Priority')
]

class Order(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    listing_date = models.DateField(help_text='To calculate sell through rate', null=True, blank=True)
    sale_price = models.FloatField(null=True, blank=True, help_text='total price including shipping')
    sale_fees = models.FloatField(null=True, blank=True)
    collected_tax = models.FloatField(null=True, blank=True, help_text='Did this marketplace collect sales tax on your behalf?')
    shipping_fees = models.FloatField(null=True, blank=True)
    shipping_method = models.CharField(
        max_length=24,
        choices=SHIPPING_TYPES,
        default='first_class'
    )
    sold_date = models.DateField('Date item was sold', null=True, blank=True)
    sold_at = models.CharField(
        max_length=24,
        choices=settings.MARKETPLACE_CHOICES,
        default='',
        null=True,
        blank=True
    )
    type = models.CharField(
        max_length=24,
        choices=LOCATION_CHOICES,
        default='domestic'
    )
    promoted = models.BooleanField(null=True, blank=True, help_text='Did this item sell due to paid advertising?')
    quantity = models.PositiveIntegerField(null=True, blank=True)
    tracking_number = models.PositiveIntegerField(null=True, blank=True)
    order_id = models.PositiveIntegerField(null=True, blank=True, help_text='For eBay')
    transaction_id = models.PositiveIntegerField(null=True, blank=True, help_text='For eBay')
    item_number = models.PositiveIntegerField(null=True, blank=True, help_text='For eBay')

    def __str__(self):
        return 'Sold ' + str(self.item)
