from django.views.generic import DetailView, ListView

from products.models import Product, Manufacturer


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'


class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
