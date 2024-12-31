# Generated by Django 5.1.4 on 2024-12-30 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField(unique=True)),
                ('last_purchase_date', models.DateField()),
                ('total_orders', models.IntegerField()),
                ('total_spent', models.FloatField()),
                ('average_order_value', models.FloatField()),
                ('days_since_last_purchase', models.IntegerField()),
                ('churned', models.BooleanField(default=False)),
            ],
        ),
    ]