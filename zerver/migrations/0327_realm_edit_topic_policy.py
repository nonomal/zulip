# Generated by Django 3.2.2 on 2021-05-26 09:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0326_alter_realm_authentication_methods"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="edit_topic_policy",
            field=models.PositiveSmallIntegerField(default=5),
        ),
    ]
