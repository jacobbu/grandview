# Generated by Django 5.1.7 on 2025-03-28 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Video",
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
                ("name", models.CharField(max_length=255)),
                ("rtsp", models.CharField(max_length=255)),
                ("created_at", models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
