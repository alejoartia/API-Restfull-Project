# Generated by Django 3.2.7 on 2021-09-08 02:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=255)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250, null=True)),
                ('price', models.FloatField(default=0.0)),
                ('stock', models.IntegerField(default=0)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=200)),
                ('nit', models.IntegerField()),
                ('code', models.CharField(max_length=255, unique=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now_add=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clients')),
            ],
        ),
        migrations.CreateModel(
            name='BillProducts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now_add=True)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bills')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.products')),
            ],
        ),
    ]
