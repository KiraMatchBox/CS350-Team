# Generated by Django 3.1.1 on 2020-12-02 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_assignment_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='title',
        ),
        migrations.AlterField(
            model_name='assignment',
            name='details',
            field=models.TextField(null=True),
        ),
    ]
