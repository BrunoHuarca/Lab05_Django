# Generated by Django 4.1.1 on 2022-09-28 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.IntegerField(default=0)),
                ('telefono', models.IntegerField(default=0)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('fecha_nacimiento', models.DateTimeField(verbose_name='fecha de nacimiento')),
                ('fecha_publicacion', models.DateTimeField(verbose_name='fecha de publicacion')),
            ],
        ),
    ]
