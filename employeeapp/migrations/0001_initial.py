# Generated by Django 4.2.5 on 2023-10-17 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_no', models.CharField(max_length=100)),
                ('dealer_code', models.CharField(max_length=100)),
                ('employee_name', models.CharField(max_length=100)),
                ('territory', models.CharField(max_length=100)),
            ],
        ),
    ]
