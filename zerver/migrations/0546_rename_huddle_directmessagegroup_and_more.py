# Generated by Django 5.0.6 on 2024-07-05 10:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0545_attachment_content_type"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.RenameModel(old_name="Huddle", new_name="DirectMessageGroup"),
                migrations.AlterModelTable(name="directmessagegroup", table="zerver_huddle"),
            ],
        )
    ]
