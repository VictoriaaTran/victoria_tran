# Generated by Django 4.2.7 on 2023-11-10 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
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
                (
                    "name",
                    models.CharField(
                        error_messages={"unique": "Name has already been taken"},
                        max_length=20,
                        unique=True,
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        error_messages={"unique": "Invalid email"},
                        max_length=254,
                        unique=True,
                    ),
                ),
                ("created_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
