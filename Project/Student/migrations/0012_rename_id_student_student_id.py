# Generated by Django 5.0.4 on 2024-05-02 13:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Student", "0011_alter_student_major"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="id",
            new_name="student_id",
        ),
    ]