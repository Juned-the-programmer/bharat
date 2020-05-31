from django.shortcuts import render,HttpResponse
from .models import product
# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def product_(request):

    data = product.objects.all().order_by('id')

    context={
        'data':data
    }

    return render(request,'pages/product.html',context)

def product_page(request,pk):

    product_data = product.objects.get(pk=pk)
    context = {
        'product_data':product_data
    }
    return render(request,'pages/product_page.html',context)