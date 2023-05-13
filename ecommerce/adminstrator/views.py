from django.shortcuts import render, redirect, get_object_or_404
from django.http.response import HttpResponseNotFound
from .forms import *
from .models import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def Category_list(request):
    context ={
        'object_list' : Category.objects.all()
    }
    return render(request, "adminstrator/category/list.html", context)


def Category_create(request):
    context ={}
    if request.method == 'GET':
        context['form'] = CategoryForm()
        return render(request, 'adminstrator/category/create.html', context)
    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else:
            context ['form'] = form
            return render(request, 'adminstrator/category/create.html', context)


def Category_update(request, id):
    context ={}
    category =get_object_or_404(Category,id = id)
    if request.method =='GET':
        context ['form'] = CategoryForm(instance = category)
        return render(request, 'adminstrator/category/create.html', context)
    elif request.method == 'POST':
        form = CategoryForm(data=request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        else :
            context ['form'] = form
            return render(request, 'adminstrator/category/create.html')


def category_delete(request, id):
    category = get_object_or_404(Category,id = id)
    category.delete()
    return redirect('category_list')


class BrandListView(ListView):
    model = Brand
    template_name = 'adminstrator/brand/list.html'


class BrandCreateView(CreateView):
    model = Brand
    template_name = 'adminstrator/brand/create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand_list')


class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'adminstrator/brand/create.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('brand_list')

class BrandDeleteView(DeleteView):
    model = Brand
    template_name = 'adminstrator/brand/delete.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('brand_list')

class ProductListView(ListView):
    model = Products
    template_name = 'adminstrator/product/list.html'
    queryset = Products.objects.all().select_related 

def Product_create(request):
    context ={}
    if request.method == 'GET':
        context ['form'] = ProductsForm()
        return render(request, 'adminstrator/product/create.html', context)
    elif request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES)
        if form.is_valid():
            
            form.save()
            return redirect('product_list')
        context ['form'] = form
        return render(request, 'adminstrator/product/create.html', context)\

def product_update(request,id):
    context ={}
    product = get_object_or_404(Products, id =id)
    if request.method == 'GET':
        context ['form'] = ProductsForm(instance = product)
        return render(request, 'adminstrator/product/create.html', context)
    elif request.method == 'POST':
        form = ProductsForm(request.POST, request.FILES, instance = product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        else :
            context ['form'] = form
            return  render(request, 'adminstrator/product/create.html',context)

def Product_delete(request, id):
    product = get_object_or_404(Products,id = id)
    product.status = 'Inactive'
    product.save()
    return redirect('product_list')
    

        



    

