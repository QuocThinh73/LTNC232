# Generated by Django 5.0.4 on 2024-05-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Databases", "0008_semester_is_registration"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="days",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="subject",
            name="hours",
            field=models.IntegerField(default=1),
        ),
    ]