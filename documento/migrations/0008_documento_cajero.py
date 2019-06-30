# Generated by Django 2.1.5 on 2019-05-06 09:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documento', '0007_auto_20190505_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='cajero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Cajero'),
        ),
    ]