# Generated by Django 5.0.4 on 2024-04-24 16:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Student", "0006_remove_student_enrollment_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="department",
        ),
        migrations.RemoveField(
            model_name="student",
            name="major",
        ),
    ]
