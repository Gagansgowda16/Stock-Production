# Generated by Django 3.0.7 on 2023-12-14 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forus_Webapp', '0020_auto_20231128_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockbin',
            name='item',
            field=models.CharField(default=0, max_length=60),
        ),
    ]
