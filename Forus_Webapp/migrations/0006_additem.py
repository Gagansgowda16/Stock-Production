# Generated by Django 3.0.7 on 2023-11-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forus_Webapp', '0005_stockbin_rdno'),
    ]

    operations = [
        migrations.CreateModel(
            name='additem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('total', models.CharField(max_length=60)),
            ],
        ),
    ]
