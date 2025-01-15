# Generated by Django 4.2.5 on 2023-09-13 05:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0028_rename_extradatajson_remoteauditlog_extra_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remoterealmauditlog",
            name="realm_id",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="remoterealmauditlog",
            name="remote_id",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="remoterealmcount",
            name="realm_id",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="remoterealmcount",
            name="remote_id",
            field=models.IntegerField(),
        ),
        migrations.AddConstraint(
            model_name="remoterealmauditlog",
            constraint=models.UniqueConstraint(
                fields=("server", "remote_id"), name="zilencer_remoterealmauditlog_server_remote"
            ),
        ),
        migrations.AddIndex(
            model_name="remoterealmauditlog",
            index=models.Index(
                fields=["server", "realm_id", "remote_id"],
                name="zilencer_remoterealmauditlog_server_realm_remote",
            ),
        ),
    ]
