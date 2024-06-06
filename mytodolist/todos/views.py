from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todos/todo_list.html', {'items': items})

def add_todo(request):
    new_item = TodoItem(title=request.POST['title'])
    new_item.save()
    return redirect('/todos/')

def complete_todo(request, todo_id):
    item = TodoItem.objects.get(pk=todo_id)
    item.completed = True
    item.save()
    return redirect('/todos/')