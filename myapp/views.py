# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject

# Create your views here.

def index(request):
	title = "Welcome to Django !!"
	return render(request, "index.html", {
		'title': title
	})

def about(request):
	username = 'fazts'
	return render(request, "about.html", {
		'username': username
	})

def hello(request, id):
	return HttpResponse("Hello %s" % id )


def projects(request):
	# projects = list(Project.objects.values())
	# return JsonResponse(projects, safe=False)
	projects = Project.objects.all()
	return render(request, "projects/projects.html", {
		'projects': projects
	})

def tasks(request):
	# task = Task.objects.get(id=id)
	# task = get_object_or_404(Task, id=id)
	# return HttpResponse("task: %s" %task.title)
	tasks = Task.objects.all()
	return render(request, "tasks/tasks.html", {
		'tasks': tasks
	})

def create_task(request):


	if request.method == 'GET':
		return render(request, "tasks/create_task.html", {
			'form': CreateNewTask()
		})
	else:
		Task.objects.create(
			title=request.POST['title'], 
			description=request.POST['description'],
			project_id=2
		)
		return redirect('tasks')


def create_project(request):
	if request.method == "GET":
		return render(request, "projects/create_project.html", {
			'form': CreateNewProject()
		})
	else:
			project = Project.objects.create(name=request.POST["name"])
			redirect('projects')