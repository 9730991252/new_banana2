# Generated by Django 5.1.3 on 2025-02-22 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunil', '0003_shope_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shope_payment',
            name='amount',
            field=models.FloatField(),
        ),
    ]
