from django.contrib import admin
from .models import Category, Material, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price",)
    search_fields = ("title", "price", "stock",)
    list_filter = ("title", "category", "main_material", "price", "stock",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Material)