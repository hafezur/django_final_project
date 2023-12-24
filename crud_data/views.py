from django.shortcuts import render,redirect
from crud_data.models import shop_data
from crud_data.forms import shop_dataForm 
from django.contrib.auth import authenticate
from django.db.models import Q
from .models import shop_data
# Create your views here

def find_data(request):
    value=shop_data.objects.all()
    
    #print(value)
    return render(request, 'data_table.html',  {'value': value})


def store_data(request):
    if request.method =='POST':
        value=shop_dataForm(request.POST)
        if value.is_valid():
            value.save()
            #print(value.cleaned_data)
            return redirect('find_data')
    else:
        value=shop_dataForm()
    return render(request,'create_data.html',{'form': value})

def edit_data(request,id):
    value=shop_data.objects.get(pk=id)
    #print(value)
    form=shop_dataForm(instance=value)
    if request.method == 'POST':
        form=shop_dataForm(request.POST, instance=value)
        if form.is_valid():
            form.save()
            return redirect('find_data')
    return render(request,'update_data.html', {'form': form })

def delete_data(request,id):
    value=shop_data.objects.get(pk=id).delete()
    return redirect('find_data')

def search(request): # this is for searching.
    value=[]
    product_count=0
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            value = shop_data.objects.order_by('-trade_code').filter(Q(trade_code__icontains=keyword) | Q(high__icontains=keyword))
            product_count = value.count() # Q= when use multiple logical filter in model we will ues Q. and icontains= case insensetive
            print(value)
    context = {
        'value': value,
        'p_count': product_count,
    }
    return render(request, 'data_table.html', context)

