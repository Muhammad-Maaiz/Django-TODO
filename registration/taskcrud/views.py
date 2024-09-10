from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User


def add_task(request):    
    result = ""
    user = User.objects.get(id=request.user.id)  
    if request.method=="POST":
        task_title = request.POST.get('task_title')
        task_desc = request.POST.get('task_description')
        task_date = request.POST.get('task_due_date')
        task = Task(user=user, task_title=task_title, task_description=task_desc, task_due_date=task_date)
        task.save()

        result = "Task Added Successfully"

    return render(request, 'addtask.html', {'result': result})

def update_task(request, id):
    user = request.user
    task = Task.objects.get(id=id, user=user)  

    if request.method == "POST":
        task_title = request.POST.get('task_title')
        task_desc = request.POST.get('task_description')
        task_date = request.POST.get('task_due_date')
        
        # Updating the task with new data
        task.task_title = task_title
        task.task_description = task_desc
        task.task_due_date = task_date
        task.save()

        return redirect('viewtask')

    return render(request, 'updatetask.html', {'task': task})    

def view_task(request):
    user = request.user  
    tasks = Task.objects.filter(user=user) 

    return render(request, 'viewtask.html', {'tasks': tasks})

def delete_task(request, id):
    user = request.user
    task = Task.objects.get(id=id, user=user)  
    if request.method=="POST":
        task.delete()
        return redirect('viewtask')  

    return render(request, 'deletetask.html',{'task':task})

