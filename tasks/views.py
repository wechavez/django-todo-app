from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task

def tasks(request):

  if request.method == 'GET':
    tasks = Task.objects.all()
    

    return render(request, 'tasks/index.html', {
      'tasks': tasks,
    })
  
  else:
    title = request.POST.get('title')
    Task.objects.create(title=title)

    return redirect('index')
