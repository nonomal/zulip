# Generated by Django 4.2 on 2023-05-09 00:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0448_scheduledmessage_new_fields"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="scheduledmessage",
            index=models.Index(
                condition=models.Q(("delivered", False), ("failed", False)),
                fields=["scheduled_timestamp"],
                name="zerver_unsent_scheduled_messages_by_time",
            ),
        ),
        migrations.AddIndex(
            model_name="scheduledmessage",
            index=models.Index(
                condition=models.Q(("delivered", False)),
                fields=["sender", "delivery_type", "scheduled_timestamp"],
                name="zerver_unsent_scheduled_messages_by_user",
            ),
        ),
    ]
