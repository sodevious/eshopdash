from django.db import models

class Marketplace(models.Model):
    name = models.CharField(max_length=255)
    sales_tax = models.FloatField(help_text="Do you pay sales tax to purchase here?", null=True, blank=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return str(self.name)


# import csv from Ebay
# assign items to current items (merge)
# or add new items if they dont exist
# create a fixure file
