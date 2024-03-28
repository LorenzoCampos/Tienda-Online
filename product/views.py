from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, Material
import requests

# def products_index(request):
#     products = Product.objects.all()
#     categories = Category.objects.all()
#     materials = Material.objects.all()
#     context = {
#         'products': products,
#         'categories': categories,
#         'materials': materials
#     }
#     return render(request, 'products/index.html', context)


# def filterProducts(request, main_material_id = None, category_id = None):
#     categories = Category.objects.all()
#     materials = Material.objects.all()
#     context = {
#         'categories': categories,
#         'materials': materials,
#     }
    
#     if main_material_id is not None:
#         filter_obj = get_object_or_404(Material, pk=main_material_id)
#         products = Product.objects.filter(main_material=filter_obj)
#     elif category_id is not None:
#         filter_obj = get_object_or_404(Category, pk=category_id)
#         products = Product.objects.filter(category=filter_obj)
#     else:
#         return redirect('products_index')
    
#     if not products:
#         message = "No se encontraron resultados."
#         context.update({'message': message})
#     else:
#         context.update({'products': products})
#     return render(request, 'products/index.html', context)


# def products_index(request):
#     products = Product.objects.all()
#     if request.GET.get('category') is not None:
#         products = products.objects.filter(category=request.GET.get('category'))
#     if request.GET.get('material') is not None:
#         products = products.objects.filter(main_material=request.GET.get('material'))
#     if request.GET.get('price') is not None:
#         if request.GET.get('price') == '1':
#             products = products.order_by('-price')
#         if request.GET.get('price') == '0':
#             products = products.order_by('price')
#     categories = Category.objects.all()
#     materials = Material.objects.all()
#     context = {
#         'products': products,
#         'categories': categories,
#         'materials': materials
#     }
#     return render(request, 'products/index.html', context)


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
        'selected_material': material  # Pasar el material seleccionado de nuevo al contexto
    }
    return render(request, 'products/index.html', context)


def detail(request, id):
    item = Product.objects.get(id=id)
    context = {
        'item': item
    }
    return render(request, 'products/detail.html', context)