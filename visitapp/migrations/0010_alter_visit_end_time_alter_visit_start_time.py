# Generated by Django 4.2.5 on 2023-11-23 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitapp', '0009_alter_visit_end_time_alter_visit_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='end_time',
            field=models.TimeField(default='04:14:40', null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='start_time',
            field=models.TimeField(default='04:14:40', null=True),
        ),
    ]
