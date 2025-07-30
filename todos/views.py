from django.shortcuts import redirect
from .models import Task

def addTask(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')  # 'task' is the name attribute of your input field
        if task_text:
            Task.objects.create(task=task_text)
        return redirect('home')  
    # return redirect('home') 
