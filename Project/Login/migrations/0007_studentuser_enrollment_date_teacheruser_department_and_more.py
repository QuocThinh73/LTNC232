# Generated by Django 5.0.4 on 2024-04-18 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_myuser_user_type_studentuser_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='enrollment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacheruser',
            name='department',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='myuser_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Login.myuser'),
        ),
        migrations.AlterField(
            model_name='teacheruser',
            name='myuser_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Login.myuser'),
        ),
    ]