# Generated by Django 5.0.4 on 2024-05-01 05:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0005_alter_teacher_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='degrees',
        ),
        migrations.AddField(
            model_name='degrees',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Teacher.teacher'),
        ),
    ]
