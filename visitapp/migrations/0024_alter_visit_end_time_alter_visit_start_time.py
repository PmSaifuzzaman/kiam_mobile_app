# Generated by Django 5.0.6 on 2024-06-30 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitapp', '0023_alter_visit_end_time_alter_visit_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='end_time',
            field=models.TimeField(default='04:07:45', null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='start_time',
            field=models.TimeField(default='04:07:45', null=True),
        ),
    ]
