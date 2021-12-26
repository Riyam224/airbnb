# Generated by Django 4.0 on 2021-12-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='children',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=2),
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='guest',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=2),
        ),
    ]