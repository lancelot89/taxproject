# Generated by Django 3.1.4 on 2020-12-07 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaxModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_tax', models.IntegerField()),
                ('resident_tax', models.IntegerField()),
                ('health_insurance_tax', models.IntegerField()),
                ('max_housetown_tax', models.IntegerField()),
            ],
        ),
    ]
