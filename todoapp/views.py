from django.shortcuts import render, redirect
from .models import MyTodo
from .forms import MyTodoForm

# Create your views here.
def alltodo(request):
    todos = MyTodo.objects.all()
    form = MyTodoForm()
    if request.method == 'POST':
        form = MyTodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alltodo')
    return render(request, 'alltodo.html', {'todos':todos, 'form': form})


def updateItem(request, pk):
    item = MyTodo.objects.get(id = pk)
    form = MyTodoForm(instance=item)
    if request.method == 'POST':
        form = MyTodoForm(request.POST, instance = item)
        if form.is_valid():
            form.save()
            return redirect('alltodo')
    return render(request, 'update.html', {'item': item, 'form':form})

def deleteItem(request, pk):
    item = MyTodo.objects.get(id = pk)
    item.delete()
    return redirect('alltodo')