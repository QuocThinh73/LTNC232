# Generated by Django 5.0.4 on 2024-05-03 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0009_merge_20240503_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='course_file',
        ),
        migrations.RemoveField(
            model_name='course',
            name='description',
        ),
        migrations.RemoveField(
            model_name='course',
            name='syllabus',
        ),
    ]
