# Generated by Django 4.1.2 on 2022-12-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piso', models.IntegerField(verbose_name='Piso')),
                ('numero', models.CharField(max_length=2, verbose_name='Número')),
                ('expensas', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Expensas %')),
                ('propietario', models.IntegerField(verbose_name='Propietario')),
                ('edificio', models.IntegerField(verbose_name='Edificio')),
            ],
            options={
                'verbose_name': 'Departamento',
                'verbose_name_plural': 'Departamentos',
                'db_table': 'departamento',
                'ordering': [],
                'managed': True,
            },
        ),
    ]
