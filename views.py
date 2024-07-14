from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, ProductCategory
from django.http import Http404
from django.db.models import Avg, Min, Max

# Create your views here.


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 1


    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        data = base_query.filter(is_active=True)
        return data

# def product_list(request):
#     products = Product.objects.all().order_by('-price')[:5]
#     return render(request, 'product_module/product_list.html', {
#         'products': products,
#     })

class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product



# def product_detail(request, slug):
#     # Product_d = ProductCategory.objects.get(id=p_id)
#     product = get_object_or_404(Product, slug=slug)
#     # slug_d = Product_d.slug
#     return render(request, 'product_module/product_detail.html',
#                   {'product': product}
#                   )
