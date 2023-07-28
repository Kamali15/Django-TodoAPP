from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm


# Create your views here.


# def base(request):
#     return render(request,"header.html")

def home(request):
    key = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request, "lists.html", {"data": key, "forms": form})


def update_task(request, pk):
    tasks = Task.objects.get(id=pk)
    form = TaskForm(instance=tasks)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, "update.html", {"forms": form})


def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'delete.html', context)
