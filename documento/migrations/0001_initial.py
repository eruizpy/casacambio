# Generated by Django 2.2.3 on 2019-09-29 02:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import fuente.utils
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cuenta', '0001_initial'),
        ('almacen', '0001_initial'),
        ('persona', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentoTipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('modo', models.CharField(choices=[('ENTRADA', 'Entrada'), ('SALIDA', 'Salida'), ('TRANSFERENCIA', 'Transferencia'), ('FACTURA', 'Factura'), ('COTIZACION', 'Cotización'), ('ORDEN', 'Orden')], max_length=20, verbose_name='Modo')),
                ('tags', models.CharField(blank=True, editable=False, max_length=512)),
            ],
            options={
                'verbose_name': 'Tipo de documento',
                'verbose_name_plural': 'Tipos de documentos',
            },
            bases=(models.Model, fuente.utils.Texto),
        ),
        migrations.CreateModel(
            name='HistoricalDocumentoTipo',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('codigo', models.CharField(db_index=True, max_length=10, verbose_name='Código')),
                ('nombre', models.CharField(db_index=True, max_length=50, verbose_name='Nombre')),
                ('modo', models.CharField(choices=[('ENTRADA', 'Entrada'), ('SALIDA', 'Salida'), ('TRANSFERENCIA', 'Transferencia'), ('FACTURA', 'Factura'), ('COTIZACION', 'Cotización'), ('ORDEN', 'Orden')], max_length=20, verbose_name='Modo')),
                ('tags', models.CharField(blank=True, editable=False, max_length=512)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Tipo de documento',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDocumento',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('numero', models.IntegerField(db_index=True, default=-1, editable=False, verbose_name='Número')),
                ('fecha', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('fecha_creacion', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('monto_entrada', models.DecimalField(blank=True, decimal_places=2, help_text='Monto que trae el cliente', max_digits=17, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Monto de entrada')),
                ('monto_salida', models.DecimalField(blank=True, decimal_places=2, help_text='Monto que se le entregará al cliente', max_digits=17, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Monto de salida')),
                ('tasa_entrada', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Tasa de entrada (compra)', max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tasa de entrada')),
                ('tasa_salida', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Tasa de salida (venta)', max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tasa de salida')),
                ('tasa_entrada_para_venta_del_dia', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Tasa de venta del día')),
                ('ganancia', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=17, verbose_name='Ganancia')),
                ('is_print', models.BooleanField(default=False, verbose_name='¿Se imprimió?')),
                ('nota', models.TextField(blank=True, verbose_name='Nota')),
                ('tags', models.TextField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('almacen', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='almacen.Almacen', verbose_name='Almacén')),
                ('cajero', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cajero')),
                ('entrada', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cuenta.Cuenta', verbose_name='Entrada')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('persona', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='persona.Persona', verbose_name='Persona')),
                ('salida', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cuenta.Cuenta', verbose_name='Salida')),
                ('tipo', models.ForeignKey(blank=True, db_constraint=False, help_text='Tipo de documento', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='documento.DocumentoTipo')),
            ],
            options={
                'verbose_name': 'historical Documento',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(default=-1, editable=False, unique=True, verbose_name='Número')),
                ('fecha', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('monto_entrada', models.DecimalField(blank=True, decimal_places=2, help_text='Monto que trae el cliente', max_digits=17, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Monto de entrada')),
                ('monto_salida', models.DecimalField(blank=True, decimal_places=2, help_text='Monto que se le entregará al cliente', max_digits=17, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Monto de salida')),
                ('tasa_entrada', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Tasa de entrada (compra)', max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tasa de entrada')),
                ('tasa_salida', models.DecimalField(blank=True, decimal_places=2, default=None, help_text='Tasa de salida (venta)', max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tasa de salida')),
                ('tasa_entrada_para_venta_del_dia', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=5, verbose_name='Tasa de venta del día')),
                ('ganancia', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=17, verbose_name='Ganancia')),
                ('is_print', models.BooleanField(default=False, verbose_name='¿Se imprimió?')),
                ('nota', models.TextField(blank=True, verbose_name='Nota')),
                ('tags', models.TextField(blank=True, editable=False)),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='almacen.Almacen', verbose_name='Almacén')),
                ('cajero', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Cajero')),
                ('entrada', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entrada_set', to='cuenta.Cuenta', verbose_name='Entrada')),
                ('persona', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='persona.Persona', verbose_name='Persona')),
                ('salida', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salida_set', to='cuenta.Cuenta', verbose_name='Salida')),
                ('tipo', models.ForeignKey(help_text='Tipo de documento', on_delete=django.db.models.deletion.CASCADE, to='documento.DocumentoTipo')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
                'ordering': ['-fecha', '-id'],
            },
            bases=(models.Model, fuente.utils.Texto),
        ),
    ]
