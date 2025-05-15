from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404


# Create your views here.
def products_view(request):  #fb
    products = Product.objects.all()
    context = {
        'products_list': products
    }
    return render(request, 'products_list.html', context)


class ProductsView(ListView):
    template_name = 'products_list.html'

    def get_context_data(self, *args, object_list=None, **kwargs):  #passinf qs to context
        context = super(ProductsView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        return Product.objects.all()


#readmore
def product_detail(request, product_id):  #for more detail
    #product = Product.objects.get(id=product_id)
    #product = get_object_or_404(Product,id=product_id)

    product = Product.objects.get_product_by_id(product_id)
    if product is None:
        raise Http404("Product not found")

    # qs = Product.objects.filter(id=product_id)
    # if qs.exists() and qs.count() == 1:
    #     product= qs.first
    # else:
    #     raise Http404("Product not found")

    context = {
        'product': product,
    }
    return render(request, 'product_detail.html', context)


class ProductsDetail(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'

    def get_context_data(self, *args, object_list=None, **kwargs):  #passinf qs to context
        context = super(ProductsDetail, self).get_context_data(*args, **kwargs)
        return context

    def get_object(self, *args, **kwargs):
        productid = self.kwargs.get('pk')
        product = Product.objects.get_product_by_id(productid)

        if product is None:
            raise Http404("Product not found")
        return product


class ProductsActiveList(ListView):
    template_name = 'products_list.html'

    def get_queryset(self):#chainig
        return Product.objects.get_active_show_products()


class ProductsActiveDetail(DetailView):
    template_name = 'product_detail.html'

    def get_queryset(self):
        return Product.objects.get_active_products()
