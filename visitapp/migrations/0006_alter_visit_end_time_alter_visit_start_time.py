# Generated by Django 4.2.5 on 2023-11-21 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitapp', '0005_alter_visit_end_time_alter_visit_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='end_time',
            field=models.TimeField(default='11:07:53', null=True),
        ),
        migrations.AlterField(
            model_name='visit',
            name='start_time',
            field=models.TimeField(default='11:07:53', null=True),
        ),
    ]
