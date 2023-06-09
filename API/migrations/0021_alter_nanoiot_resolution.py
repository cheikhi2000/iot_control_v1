# Generated by Django 4.2 on 2023-05-03 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("API", "0020_alter_nanoiot_resolution"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nanoiot",
            name="resolution",
            field=models.CharField(
                choices=[
                    ("1366x673", "1366x673"),
                    ("3840x2400", "3840x2400"),
                    ("3840x2160", "3840x2160"),
                    ("2880x1800", "2880x1800"),
                    ("2560x1600", "2560x1600"),
                    ("2560x1440", "2560x1440"),
                    ("1920x1440", "1920x1440"),
                    ("1856x1392", "1856x1392"),
                    ("1792x1344", "1792x1344"),
                    ("1920x1200", "1920x1200"),
                    ("1920x1080", "1920x1080"),
                    ("1600x1200", "1600x1200"),
                    ("1680x1050", "1680x1050"),
                    ("1400x1050", "1400x1050"),
                    ("1280x1024", "1280x1024"),
                    ("1440x900", "1440x900"),
                    ("1280x960", "1280x960"),
                    ("1360x768", "1360x768"),
                    ("1280x800", "1280x800"),
                    ("1152x864", "1152x864"),
                    ("1280x768", "1280x768"),
                    ("1280x720", "1280x720"),
                    ("1024x768", "1024x768"),
                    ("800x600", "800x600"),
                    ("640x480", "640x480"),
                ],
                default="1920x1080",
                max_length=20,
            ),
        ),
    ]
