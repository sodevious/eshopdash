# Generated by Django 3.0.3 on 2020-02-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20200208_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='purchase_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Date item was sold'),
        ),
        migrations.AddField(
            model_name='item',
            name='purchase_price',
            field=models.FloatField(blank=True, help_text='include sales tax if any', null=True),
        ),
    ]