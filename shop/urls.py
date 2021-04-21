from re import A
from shop.models import Category
from django.contrib import admin
from django.urls import path

from .views import product_detail, product_list, SearchResultsListView, ProductList, AboutPage, DeliveryInfo, AllProducts

app_name = 'shop'

urlpatterns = [
    path('products/', AllProducts.as_view(), name='product_list'),
    path('delivery_info/', DeliveryInfo.as_view(), name='deliv'),
    path('<int:id>/<str:slug>/', product_detail, name='product_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('about/', AboutPage.as_view(), name='about'),
    path('', ProductList.as_view(), name='home'),
]
