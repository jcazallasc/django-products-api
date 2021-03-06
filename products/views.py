from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from products.models import Manufacturer, Product


def product_list(request):
    products = Product.objects.all()
    data = {'products': list(products.values())}

    return JsonResponse(data)

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {
            'product': {
                'name': product.name,
                'manufacturer': product.manufacturer.name,
                'description': product.description,
                'photo': product.photo.url,
                'price': product.price,
                'shipping_cost': product.shipping_cost,
                'quantity': product.quantity,
            }
        }
        response = JsonResponse(data)
    except ObjectDoesNotExist:
        return JsonResponse(
            {
                'error': {
                    'code': 404,
                    'message': 'Product not found',
                }
            },
            status=404,
        )

    return response


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {'manufacturers': list(manufacturers.values())}

    return JsonResponse(data)


def manufacturer_detail(request, pk):
    try:
        manufacturer = Manufacturer.objects.filter(active=True).get(pk=pk)
        data = {
            'manufacturer': {
                'name': manufacturer.name,
                'location': manufacturer.location,
                'pruducts': list(manufacturer.products.all().values()),
            }
        }
        response = JsonResponse(data)
    except ObjectDoesNotExist:
        return JsonResponse(
            {
                'error': {
                    'code': 404,
                    'message': 'Manufacturer not found',
                }
            },
            status=404,
        )

    return response

