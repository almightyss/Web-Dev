from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:id>/', views.products_by_id),
    path('products/', views.products_list),
    path('categories/', views.categories_list),
    path('categories/<int:id>/', views.categories_by_id),
    path('categories/<int:id>/products', views.category_products)
]
