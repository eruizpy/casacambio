# Generated by Django 2.2.3 on 2019-09-29 02:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import fuente.utils
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simbolo', models.CharField(max_length=3, unique=True, verbose_name='Símbolo')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('tasa_compra', models.DecimalField(decimal_places=2, help_text='Tasa en la que la Empresa le compra al cliente.', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tasa de compra')),
                ('tasa_venta', models.DecimalField(decimal_places=2, help_text='Tasa en la que la Empresa le vende al cliente.', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tasa de venta')),
                ('is_principal', models.BooleanField(default=False, help_text='Indica que esta moneda es la principal (solo puede existir una sola moneda como principal)', verbose_name='¿Es principal?')),
                ('tags', models.CharField(blank=True, editable=False, max_length=512)),
            ],
            options={
                'verbose_name': 'Moneda',
                'verbose_name_plural': 'Monedas',
            },
            bases=(models.Model, fuente.utils.Texto),
        ),
        migrations.CreateModel(
            name='MonedaTasasUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('items', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Actualización de tasas',
                'verbose_name_plural': 'Actualizaciones de tasas',
            },
        ),
        migrations.CreateModel(
            name='HistoricalMoneda',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('simbolo', models.CharField(db_index=True, max_length=3, verbose_name='Símbolo')),
                ('nombre', models.CharField(db_index=True, max_length=50, verbose_name='Nombre')),
                ('tasa_compra', models.DecimalField(decimal_places=2, help_text='Tasa en la que la Empresa le compra al cliente.', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tasa de compra')),
                ('tasa_venta', models.DecimalField(decimal_places=2, help_text='Tasa en la que la Empresa le vende al cliente.', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tasa de venta')),
                ('is_principal', models.BooleanField(default=False, help_text='Indica que esta moneda es la principal (solo puede existir una sola moneda como principal)', verbose_name='¿Es principal?')),
                ('tags', models.CharField(blank=True, editable=False, max_length=512)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Moneda',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
