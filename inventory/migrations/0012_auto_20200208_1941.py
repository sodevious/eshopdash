# Generated by Django 3.0.3 on 2020-02-08 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplaces', '0001_initial'),
        ('inventory', '0011_auto_20200208_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='purchased_marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='marketplaces.Marketplace'),
        ),
        migrations.AddField(
            model_name='item',
            name='purchased_marketplace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='marketplaces.Marketplace'),
        ),
    ]
