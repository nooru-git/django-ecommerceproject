from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs= {'class': 'form-control', 'rows': 3}),
        } 

class BrandForm(forms.ModelForm):
     class Meta:
         model = Brand
         fields = "__all__"
         widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs= {'class': 'form-control', 'rows': 3}),
            'website': forms.URLInput(attrs= {'class' : 'form-control'})

         }

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
        widgets = {
        'name': forms.TextInput(attrs= {'class': 'form-control'}),
        'slug': forms.TextInput(attrs={'class': 'form-control'}),
        'shot_description': forms.Textarea(attrs= {'class': 'form-control', 'rows': 2}),
        'long_description': forms.Textarea(attrs= {'class': 'form-control', 'rows': 3}),
        'price': forms.NumberInput(attrs= {'class': 'form-control'}),
        'stock': forms.NumberInput(attrs= {'class': 'form-control'}),
        'category':forms.Select(attrs= {'class': 'form-control'}),
        'brand': forms.Select(attrs= {'class': 'form-control'}),
        'image':forms.FileInput(attrs= {'class': 'form-control'}),
        'status': forms.Select(attrs= {'class': 'form-control'}),  
    }   
