from django.http import JsonResponse
from .models import Category, Product

def products_list(request):
    data = list(Product.objects.values())
    return JsonResponse(data, safe=False)


def products_by_id(request, id):
    data = list(Product.objects.filter(id=id).values())
    return JsonResponse(data, safe=False)


def categories_list(request):
    data = list(Category.objects.values())
    return JsonResponse(data, safe=False)

def categories_by_id(request, id):
    data = list(Category.objects.filter(id=id).values())
    return JsonResponse(data, safe=False)

def category_products(request, id):
    data = list(Product.objects.filter(category_id=id).values())
    return JsonResponse(data, safe=False)
