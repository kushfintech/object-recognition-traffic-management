# Generated by Django 4.2.7 on 2023-11-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recognition", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="video",
            name="filename",
            field=models.CharField(default="", editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name="video",
            name="video_file",
            field=models.FileField(upload_to="recognition/static/media_saved/videos"),
        ),
    ]
