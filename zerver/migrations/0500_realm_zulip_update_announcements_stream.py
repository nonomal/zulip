# Generated by Django 4.2.9 on 2024-02-08 07:34

import django.db.models.deletion
from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps
from django.db.models import F


def set_initial_value_for_zulip_update_announcements_stream(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    Realm = apps.get_model("zerver", "Realm")
    Realm.objects.exclude(new_stream_announcements_stream__isnull=True).update(
        zulip_update_announcements_stream=F("new_stream_announcements_stream")
    )


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0499_rename_signup_notifications_stream_realm_signup_announcements_stream"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="zulip_update_announcements_stream",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="zerver.stream",
            ),
        ),
        migrations.RunPython(
            set_initial_value_for_zulip_update_announcements_stream,
            reverse_code=migrations.RunPython.noop,
            elidable=True,
        ),
    ]
