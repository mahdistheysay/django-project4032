
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import products_view , ProductsView , product_detail , ProductsDetail , ProductsActiveList , ProductsActiveDetail


app_name = 'products'

urlpatterns = [
    path('products-fb',products_view),
    path('products-cb',ProductsView.as_view()),# چون از کلاس استفاده شد
    path('products-fb/<product_id>' , product_detail),
    path('products-cb/<pk>' , ProductsDetail.as_view()), #must
    path('products-active' , ProductsActiveList.as_view()), #must
    path('products-active/<pk>' , ProductsActiveDetail.as_view()), #must
]