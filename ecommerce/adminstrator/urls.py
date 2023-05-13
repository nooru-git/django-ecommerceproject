from django.urls import path
from .views import *

urlpatterns =[
    path('category/', Category_list, name= 'category_list'),
    path('category/create/', Category_create, name= 'category_create'),
    path('category/update/<int:id>/', Category_update, name= 'category_update'),
    path('category/delete/<int:id>/', category_delete, name= 'category_delete'),

    path('brand/', BrandListView.as_view(), name= 'brand_list'),
    path('brand/create/', BrandCreateView.as_view(), name= 'brand_create'),
    path('brand/update/<int:id>/', BrandUpdateView.as_view(), name = 'brand_update'),
    path('brand/delete/<int:id>/', BrandDeleteView.as_view(), name = 'brand_delete'),

    path('product/', ProductListView.as_view(), name='product_list'),
    path('product/create/', Product_create, name='product_create'),
    path('product/update/<id>/', product_update, name='product_update'),
    path('product/delete/<id>/', Product_delete, name='product_delete'),


]