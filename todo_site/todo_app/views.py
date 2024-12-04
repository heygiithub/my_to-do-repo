from django.shortcuts import render,redirect
from django.contrib import messages

# import todo from and models
from .forms import Todoform
from .models import Todo

# Create your views here.

def index(request):
    item = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = Todoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("todo")
    form = Todoform
    
    page = {
        'forms': form,
        'list': item,
        'title': "TODO LIST"
    }
    
    return render(request,'todo/index.html',page)

# function to remove item, it recieve todo item id as pk

def remove(request,item_id):
    item1 = Todo.objects.get(id=item_id)
    item1.delete()
    messages.info(request,"item removed!!")
    return redirect('todo')
            
