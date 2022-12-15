from django.shortcuts import render, redirect
from .models import Item

from .forms import Itemdetail

# Create your views here.

def index(request):
    item = Item.objects.all()
    context ={
        'item':item
    }
    return render(request,'index.html',context)

def detail(request,id):
    item = Item.objects.get(id=id)
    
    return render(request,'detail.html',{'item':item})

def create_item(request):
    form= Itemdetail(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("index")
    
    return render(request,"item-add.html",{'form':form})

def update_item(request,id):
    item = Item.objects.get(id=id)
    form= Itemdetail(request.POST or None,instance=item) #prefill hunxa
    
    if form.is_valid():
        form.save()
        return redirect("index")
    
    return render(request,"item-update.html",{'form':form,'item':item})

def delete_item(request,id):
    item = Item.objects.get(id=id)
    
    if request.method=="POST":
        item.delete()
        return redirect("index")
    
    return render(request,"item-delete.html",{'item':item})