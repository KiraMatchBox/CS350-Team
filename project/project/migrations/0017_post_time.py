# Generated by Django 3.1.1 on 2020-12-02 03:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20201201_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
