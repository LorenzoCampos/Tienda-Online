from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name="Categoria")
    category_description = models.TextField(max_length=100, blank=True, null=True, verbose_name="Descripcion")
    
    def __str__(self):
        return self.category_name

class Material(models.Model):
    material_name = models.CharField(max_length=100, verbose_name="Material")
    material_description = models.TextField(max_length=100, blank=True, null=True, verbose_name="Descripcion")
    
    def __str__(self):
        return self.material_name

class Product(models.Model):
    image = models.ImageField(upload_to="product_image", null=True, blank=True, verbose_name="Imagen del producto")
    title = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.TextField(max_length=200, blank=True, null=True,verbose_name="Descripcion")
    category = models.ForeignKey(Category,on_delete=models.PROTECT, blank=True, null=True, verbose_name="Categoria")
    main_material = models.ForeignKey(Material,on_delete=models.PROTECT, blank=True, null=True, verbose_name="Material")
    price = models.PositiveIntegerField(default=0, verbose_name="Precio")
    stock = models.PositiveIntegerField(default=0, verbose_name="Stock")
    
    def __str__(self):
        return self.title