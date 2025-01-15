# Generated by Django 4.2.7 on 2023-11-26 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("corporate", "0024_zulipsponsorshiprequest_fill_customer_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="zulipsponsorshiprequest",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="corporate.customer"
            ),
        ),
    ]
