# Generated by Django 3.1.7 on 2021-06-20 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_user_api_authorized"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="timezone_name",
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]
