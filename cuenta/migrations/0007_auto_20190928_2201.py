# Generated by Django 2.2.3 on 2019-09-28 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0006_auto_20190616_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta',
            name='tags',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='historicalcuenta',
            name='tags',
            field=models.TextField(blank=True, editable=False),
        ),
    ]
