# Generated by Django 4.2 on 2023-04-28 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0016_alter_nanoiot_where"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="nanoiot",
            name="image",
        ),
        migrations.AddField(
            model_name="nanoiot",
            name="screenshot<django.db.models.fields.CharField>.png",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]