from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Material
import requests


def products_index(request):
    categoria = request.GET.get('categoria')
    material = request.GET.get('material')
    orden = request.GET.get('orden')

    products = Product.objects.all()
    categories = Category.objects.all()
    materials = Material.objects.all()

    if categoria:
        try:
            categoria = int(categoria)  # Convertir a entero si no está vacío
            products = products.filter(category=categoria)
        except ValueError:
            # Manejar el caso en el que el valor no se puede convertir a entero
            pass
        
    if material:
        try:
            material = int(material)
            products = products.filter(main_material=material)
        except ValueError:
            pass

    if orden is not None:
        if orden == 'precio_desc':
            products = products.order_by('-price')
        elif orden == 'precio_asc':
            products = products.order_by('price')

    context = {
        'products': products,
        'categories': categories,
        'materials': materials,
        'selected_categoria': categoria,  # Pasar la categoría seleccionada de nuevo al contexto
        'selected_material': material,  # Pasar el material seleccionado de nuevo al contexto
        'selected_orden': orden
    }
    return render(request, 'products/index.html', context)


def detail(request, id):
    item = Product.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'products/detail.html', context)