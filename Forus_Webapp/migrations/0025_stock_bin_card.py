# Generated by Django 3.0.7 on 2024-01-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forus_Webapp', '0024_stock_bin1'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='bin_card',
            field=models.IntegerField(default=1),
        ),
    ]
