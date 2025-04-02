# Generated by Django 5.1.7 on 2025-04-02 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sunil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, null=True)),
                ('status', models.IntegerField(default=1)),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
            ],
        ),
        migrations.CreateModel(
            name='Company_opning_balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('type', models.IntegerField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.company')),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
            ],
        ),
        migrations.CreateModel(
            name='Company_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=1)),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200, null=True)),
                ('mobile', models.IntegerField()),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=1)),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='logo_images')),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
            ],
        ),
        migrations.CreateModel(
            name='office_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('pin', models.IntegerField()),
                ('status', models.IntegerField(default=1)),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer_payment_transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('bank_number', models.IntegerField(null=True)),
                ('phonepe_number', models.IntegerField(null=True)),
                ('payment_type', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.farmer')),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
                ('office_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.office_employee')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer_bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicale_number', models.CharField(max_length=100)),
                ('total_vehicale_weight', models.IntegerField(null=True)),
                ('empty_vehicale_weight', models.IntegerField(null=True)),
                ('weight', models.IntegerField()),
                ('empty_box', models.IntegerField()),
                ('leaf_weight', models.IntegerField(default=0)),
                ('wasteage', models.IntegerField()),
                ('prise', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('paid_status', models.IntegerField(default=0)),
                ('labor_amount', models.FloatField(null=True)),
                ('date', models.DateField()),
                ('bill_number', models.IntegerField(null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('farmer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.farmer')),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
                ('office_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.office_employee')),
            ],
        ),
        migrations.AddField(
            model_name='farmer',
            name='office_employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.office_employee'),
        ),
        migrations.CreateModel(
            name='company_recived_payment_transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('bank_number', models.IntegerField(null=True)),
                ('phonepe_number', models.IntegerField(null=True)),
                ('payment_type', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.company')),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
                ('office_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.office_employee')),
            ],
        ),
        migrations.CreateModel(
            name='Company_bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicale_number', models.CharField(max_length=100)),
                ('total_vehicale_weight', models.IntegerField(null=True)),
                ('empty_vehicale_weight', models.IntegerField(null=True)),
                ('weight', models.IntegerField()),
                ('empty_box', models.IntegerField()),
                ('wasteage', models.IntegerField()),
                ('prise', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('paid_status', models.IntegerField(default=0)),
                ('labor_amount', models.FloatField(null=True)),
                ('service_charge', models.FloatField(null=True)),
                ('eater', models.FloatField(null=True)),
                ('date', models.DateField(null=True)),
                ('bill_number', models.IntegerField(null=True)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('leaf_weight', models.IntegerField(default=0)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.company')),
                ('shope', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='sunil.shope')),
                ('office_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.office_employee')),
            ],
        ),
        migrations.CreateModel(
            name='Signature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='images')),
                ('office_employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='owner.office_employee')),
            ],
        ),
    ]
