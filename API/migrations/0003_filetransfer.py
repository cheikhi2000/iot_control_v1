# Generated by Django 4.2 on 2023-04-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0002_nanoiot_custom_cmd_nanoiot_custom_cmd_output_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="FileTransfer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="screenshots/")),
            ],
        ),
    ]
