# Generated by Django 3.1.1 on 2020-09-29 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20200928_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='title',
            field=models.CharField(default='Student Submission', max_length=50),
            preserve_default=False,
        ),
    ]
