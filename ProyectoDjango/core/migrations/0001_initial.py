# Generated by Django 4.2.1 on 2023-06-19 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la categoria')),
                ('nombre_categoria', models.CharField(max_length=20, null=True, verbose_name='Nombre de la categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la comuna')),
                ('nombre_comuna', models.CharField(max_length=20, null=True, verbose_name='Nombre de la comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id_pregunta', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la pregunta')),
                ('nombre_pregunta', models.CharField(max_length=50, null=True, verbose_name='Nombre de la pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la region')),
                ('nombre_region', models.CharField(max_length=20, null=True, verbose_name='Nombre de la region')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del rol')),
                ('nombre_rol', models.CharField(max_length=20, null=True, verbose_name='Nombre del rol')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del usuario')),
                ('nombre_usuario', models.CharField(max_length=25, verbose_name='Nombre del usuario')),
                ('apellido_usuario', models.CharField(max_length=25, verbose_name='Apellido del usuario')),
                ('telefono_usuario', models.CharField(max_length=9, verbose_name='Telefono del usuario')),
                ('correo_usuario', models.CharField(max_length=40, verbose_name='Correo del usuario')),
                ('clave_usuario', models.CharField(max_length=15, verbose_name='Contraseña del usuario')),
                ('respuesta_usuario', models.CharField(max_length=40, verbose_name='Respuesta secreta del usuario')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pregunta')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del producto')),
                ('nombre_producto', models.CharField(max_length=20, null=True, verbose_name='Nombre del producto')),
                ('desc_producto', models.CharField(max_length=500, null=True, verbose_name='Descripcion del producto')),
                ('precio_producto', models.IntegerField(null=True, verbose_name='Precio del producto')),
                ('foto_producto', models.ImageField(null=True, upload_to='', verbose_name='Imagen del producto')),
                ('stock_producto', models.IntegerField(null=True, verbose_name='Stock del producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del pedido')),
                ('total_pedido', models.IntegerField(null=True, verbose_name='Total del pedido')),
                ('estado_pedido', models.BooleanField(verbose_name='Estado del pedido ')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la direccion')),
                ('nombre_direccion', models.CharField(max_length=20, null=True, verbose_name='Nombre de la direccion')),
                ('num_direccion', models.CharField(max_length=4, null=True, verbose_name='Numero de la direccion')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.comuna')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_detalle', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la direccion')),
                ('cantidad', models.IntegerField(null=True, verbose_name='Cantidad de productos')),
                ('subtotal', models.IntegerField(null=True, verbose_name='Subtotal')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.pedido')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.producto')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.region'),
        ),
    ]
