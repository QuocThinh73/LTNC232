# Generated by Django 5.0.4 on 2024-05-03 23:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Teacher", "0011_teacher_date_of_birth_alter_degrees_year_obtained"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="hometown",
            field=models.CharField(max_length=40, null=True),
        ),
    ]
