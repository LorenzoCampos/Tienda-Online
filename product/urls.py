from django.urls import path
from . import views

urlpatterns = [
    path('list/?', views.products_index, name='products_index'),
    
    # path('price/minor/<int:minor>/', views.products_index, name='products_orderPriceMinor'),
    # path('price/elserly/<int:elderly>/', views.products_index, name='products_orderPriceElderly'),
    
    # path('material/<int:main_material_id>/', views.filterProducts, name='products_filterMainMaterial'),
    # path('category/<int:category_id>/', views.filterProducts, name='products_filterCategory'),
    
    path('deatil/<int:id>', views.detail, name='products_detail')
]