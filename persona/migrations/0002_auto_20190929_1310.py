# Generated by Django 2.2.3 on 2019-09-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpersona',
            name='direccion',
            field=models.CharField(blank=True, max_length=255, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='historicalpersona',
            name='tags',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='persona',
            name='direccion',
            field=models.CharField(blank=True, max_length=255, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='tags',
            field=models.TextField(blank=True, editable=False),
        ),
    ]
