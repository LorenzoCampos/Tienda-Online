from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Material
import requests

def products_index(request, elderly = None, minor = None):
    if elderly is not None:
        products = Product.objects.all().order_by('-price')
    elif minor is not None:
        products = Product.objects.all().order_by('price')
    else:
        products = Product.objects.all()
    categories = Category.objects.all()
    materials = Material.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'materials': materials
    }
    return render(request, 'products/index.html', context)


def filterProducts(request, main_material_id = None, category_id = None):
    categories = Category.objects.all()
    materials = Material.objects.all()
    context = {
        'categories': categories,
        'materials': materials,
    }
    
    if main_material_id is not None:
        filter_obj = get_object_or_404(Material, pk=main_material_id)
        products = Product.objects.filter(main_material=filter_obj)
    elif category_id is not None:
        filter_obj = get_object_or_404(Category, pk=category_id)
        products = Product.objects.filter(category=filter_obj)
    else:
        return redirect('products_index')
    
    if not products:
        message = "No se encontraron resultados."
        context.update({'message': message})
    else:
        context.update({'products': products})
    return render(request, 'products/index.html', context)


def detail(request, id):
    item = Product.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'products/detail.html', context)