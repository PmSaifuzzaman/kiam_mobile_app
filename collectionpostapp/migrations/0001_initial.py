# Generated by Django 5.0.6 on 2024-06-27 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('pf_no', models.CharField(max_length=50)),
                ('employee_name', models.CharField(max_length=100)),
                ('party_name', models.CharField(max_length=100)),
                ('party_code', models.CharField(max_length=50)),
                ('account_no', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
