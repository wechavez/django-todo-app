from django.shortcuts import redirect, render
from .models import Task
from .forms.tasks import CreateTask

def tasks(request):

  if request.method == 'GET':
    tasks = Task.objects.all()


    return render(request, 'tasks/index.html', {
      'tasks': tasks,
      'form': CreateTask()
    })

  else:
    title = request.POST.get('title')
    Task.objects.create(title=title)

    return redirect('index')

def delete(request, id):
  task = Task.objects.get(id=id)
  task.delete()

  return redirect('index')

def complete(request, id):
  task = Task.objects.get(id=id)
  task.completed = not task.completed
  task.save()

  return redirect('index')
