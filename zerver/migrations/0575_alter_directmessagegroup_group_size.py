# Generated by Django 5.0.6 on 2024-08-21 13:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0574_backfill_directmessagegroup_group_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="directmessagegroup",
            name="group_size",
            field=models.IntegerField(),
        ),
    ]
