from django.shortcuts import redirect,get_object_or_404,render
from .models import Task
from django.http import HttpResponse

def addTask(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')  
        if task_text:
            Task.objects.create(task=task_text)
        return redirect('home')  
    return redirect('home') 

def mark_as_done(request ,pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

def mark_as_undone(request, pk):
    task = get_object_or_404(Task,pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')
def edit_task(request, pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method=="POST":
        new_task=request.POST['task']
        get_task.task= new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task
        }
        return render(request,'edit_task.html',context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home') 
    