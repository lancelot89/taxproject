# Generated by Django 3.1.4 on 2020-12-08 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxmodel',
            name='health_insurance_tax',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='taxmodel',
            name='max_housetown_tax',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
