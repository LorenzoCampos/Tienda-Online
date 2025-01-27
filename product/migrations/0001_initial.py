# Generated by Django 5.0.3 on 2024-03-17 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Categoria')),
                ('category_description', models.TextField(blank=True, max_length=100, null=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=100, verbose_name='Material')),
                ('material_description', models.TextField(blank=True, max_length=100, null=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_image', verbose_name='Imagen del producto')),
                ('title', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, max_length=200, null=True, verbose_name='Descripcion')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Precio')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stock')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.category', verbose_name='Categoria')),
                ('main_material', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.material', verbose_name='Material')),
            ],
        ),
    ]
