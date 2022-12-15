from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterItem
from django.contrib import messages 


def register(request):
    if request.method=="POST":
        form = RegisterItem(request.POST or None)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request,f'(Welcome {username} successfully registered)')
            return redirect("index")
    else:
            form = RegisterItem()
            
    return render(request,'register.html',{'form':form})    
        
