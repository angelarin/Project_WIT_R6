# Generated by Django 4.2 on 2023-04-11 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkitem',
            name='label',
            field=models.CharField(choices=[('NEW', 'new'), ('SALE', 'sale'), ('BEST', 'best')], max_length=4),
        ),
    ]
