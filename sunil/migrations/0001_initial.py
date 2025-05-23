# Generated by Django 5.1.7 on 2025-05-06 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shope',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shope_name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=500, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('contact_details', models.CharField(max_length=500, null=True)),
                ('pin', models.IntegerField()),
                ('edit_pin', models.IntegerField(default=1234)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Sunil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shope_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('payment_type', models.CharField(max_length=100)),
                ('added_date', models.DateField(auto_now_add=True)),
                ('shope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sunil.shope')),
            ],
        ),
    ]
