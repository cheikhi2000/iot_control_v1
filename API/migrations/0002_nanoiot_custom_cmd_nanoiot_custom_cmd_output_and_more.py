# Generated by Django 4.2 on 2023-04-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="nanoiot",
            name="custom_cmd",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="nanoiot",
            name="custom_cmd_output",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="nanoiot",
            name="defined_cmds",
            field=models.CharField(
                blank=True,
                choices=[("screenshot", "screenshot"), ("upgrade", "upgrade")],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="nanoiot",
            name="hostname",
            field=models.CharField(default="dm", max_length=100, unique=True),
        ),
    ]
