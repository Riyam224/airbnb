# Generated by Django 4.0 on 2022-01-01 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('property', '0006_property_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_owner', to='auth.user'),
        ),
    ]
