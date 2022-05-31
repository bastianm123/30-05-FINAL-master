# Generated by Django 4.0.4 on 2022-05-27 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_categoria_alter_producto_imagenproducto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='numeroCliente',
            field=models.IntegerField(verbose_name='Numero Cliente'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rutCliente',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut cliente'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precioProducto',
            field=models.IntegerField(verbose_name='Precio Producto'),
        ),
    ]
