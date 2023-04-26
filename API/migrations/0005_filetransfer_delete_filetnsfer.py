# Generated by Django 4.2 on 2023-04-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0004_filetnsfer_delete_filetransfer_nanoiot_what_and_more"),
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
                ("image", models.ImageField(upload_to="screenshots")),
                ("file", models.FileField(upload_to="file")),
            ],
        ),
        migrations.DeleteModel(
            name="FileTnsfer",
        ),
    ]