# Generated by Django 4.0.7 on 2022-10-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0416_set_default_emoji_style"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customprofilefield",
            name="field_type",
            field=models.PositiveSmallIntegerField(
                choices=[
                    (4, "Date"),
                    (7, "External account"),
                    (5, "Link"),
                    (3, "List of options"),
                    (8, "Pronouns"),
                    (2, "Text (long)"),
                    (1, "Text (short)"),
                    (6, "Users"),
                ],
                default=1,
            ),
        ),
    ]
