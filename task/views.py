from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def view_task(request):
    task=Task.objects.all()
    form=TaskForm()
    
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    context={"tasks":task,"form":form}
    return render(request,'home.html',context)

def update_task(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    context={"forms":form}
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")
    
    return render (request,'update_task.html',context)

def delete_task(request,pk):
    item=Task.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect("/")
    context={"items":item}
    return render(request,"delete_task.html",context)