
from django.shortcuts import render, HttpResponse
from adminstrator.forms import *
from adminstrator.models import *


# Create your views here.
def index(request):
    context = {
        'object_list' :  Products.objects.all()
    }
    return render(request, 'user/home.html', context)

def about(request):
    return render(request, 'user/about.html')

def contact(request):
    context = {}
    if request.method == 'GET': 
        
        context['form'] = ContactForm()
        
        return render(request, 'user/contact.html', context)
    elif request.method == 'POST': 
        form = ContactForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponse(" Tanks for your message. ")
        else:
            context['form'] = form
            return render(request, 'user/contact.html', context)




