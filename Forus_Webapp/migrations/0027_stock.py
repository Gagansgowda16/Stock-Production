# Generated by Django 3.0.7 on 2024-05-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forus_Webapp', '0026_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_card', models.IntegerField(default=1)),
                ('ERP_NO', models.CharField(max_length=60)),
                ('MP_NO', models.CharField(default=0, max_length=60)),
                ('str', models.CharField(max_length=60)),
                ('devr1', models.CharField(max_length=60)),
                ('rkr', models.CharField(max_length=60)),
                ('shelf', models.CharField(default=0, max_length=60)),
                ('binr', models.CharField(max_length=60)),
                ('item', models.CharField(default=0, max_length=60)),
                ('date', models.CharField(max_length=60)),
                ('pb', models.CharField(default=0, max_length=60)),
                ('desc', models.CharField(max_length=60)),
                ('no_received', models.CharField(default=0, max_length=60)),
                ('no_issue', models.CharField(default=0, max_length=60)),
                ('sb', models.CharField(default=0, max_length=60)),
                ('rdno', models.CharField(default=0, max_length=60)),
                ('remarks', models.CharField(default='remark', max_length=60)),
            ],
        ),
    ]
