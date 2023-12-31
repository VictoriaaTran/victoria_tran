# Generated by Django 4.2.7 on 2023-11-15 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0002_contact_notes_alter_contact_email_alter_contact_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(
                error_messages={
                    "invalid": "Enter a valid email address.",
                    "required": "Email field cannot be empty.",
                    "unique": "This email is already in use.",
                },
                max_length=254,
                unique=True,
            ),
        ),
    ]
