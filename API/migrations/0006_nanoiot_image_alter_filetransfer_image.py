# Generated by Django 4.2 on 2023-04-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0005_filetransfer_delete_filetnsfer"),
    ]

    operations = [
        migrations.AddField(
            model_name="nanoiot",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="filetransfer",
            name="image",
            field=models.ImageField(upload_to=""),
        ),
    ]
