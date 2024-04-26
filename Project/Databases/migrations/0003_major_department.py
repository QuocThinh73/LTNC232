# Generated by Django 5.0.4 on 2024-04-24 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Databases", "0002_department_major"),
    ]

    operations = [
        migrations.AddField(
            model_name="major",
            name="department",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Databases.department",
            ),
        ),
    ]