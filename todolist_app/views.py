from asyncio import all_tasks
from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskMate
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
# Our first view
def index(request):
    """View that determines what will render on our homepage
    """
     # A dictionary of responses
    context = {
                'index_text':"Welcome to the HomePage."
              
              }
    # return HttpResponse('Website is Live!')
    return render(request, 'index.html', context)

# Ensuring that only a logged in user gets to see the list of tasks
@login_required
def todolist(request):
    """This view takes a request from a user and returns a httpresponse
    """
    # # A dictionary of responses
    # context = {
    #             'welcome_text':"Welcome to ToDo list page."
    #           }
    # # return HttpResponse('Website is Live!')

    # Checking our request if it's a POST or GET request
    if request.method == 'POST':
        # Connecting to our form
        form = TaskForm(request.POST or None)
        # Checking if the form is valid or not
        if form.is_valid():
            # Delaying the save so that we can add more info to the form
            instance = form.save(commit= False)
            # Adding the username fo user creating the task
            instance.manage = request.user
            # Saving the forms
            instance.save()
        # Adding a message to indicate successfully added task
        messages.success(request,('New task added successfully!'))
        #Posting to our frontend
        return redirect('todolist')
    else:
        # It's a GET request
         # A list of all database objects
        all_tasks = TaskMate.objects.filter(manage = request.user)
        # Instance of pagination, we're calling it on all tasks & displaying 5 max
        paginator = Paginator(all_tasks,5)
        page = request.GET.get('page')
        # Loading tasks according to out pagination
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks': all_tasks})

# Ensuring that only a logged in user gets to see the list of tasks
@login_required
# Method to delete tasks with
def delete_task(request,task_id):
    """This view takes in a task id and deletes the task corresponding to the id
    """
    # Getting our task from the database
    task = TaskMate.objects.get(pk=task_id)
    
    if task.manage == request.user:
        # Deleting the task
        task.delete()
    else:
        messages.error(request,('Access Denied!This is not your task'))

    # Redirecting back to our todo list page
    return redirect('todolist')

# Ensuring that only a logged in user gets to see the list of tasks
@login_required
def edit_task(request,task_id):
    """This view takes a request from a user and returns a httpresponse
    """
    # Checking our request if it's a POST or GET request
    if request.method == 'POST':
        # Getting our task
        task = TaskMate.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)

        if form.is_valid():
            form.save()
        # Adding a message to indicate successfully edited task
        messages.success(request,('Task edited successfully!'))
        #Posting to our frontend
        return redirect('todolist')
    else:
        # It's a GET request
         # A list of all database objects
        task_obj = TaskMate.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj':task_obj })

# Ensuring that only a logged in user gets to see the list of tasks
@login_required
# Method to update complete tasks with
def complete_task(request,task_id):
    """This view takes in a task id and deletes the task corresponding to the id
    """
    # Getting our task from the database
    task = TaskMate.objects.get(pk=task_id)
    if task.manage == request.user:
        # Updating the done field to true
        task.done = True
        task.save()
    else:
        # An error message
        messages.error(request,('Access denied. This is not your task!'))
    # Redirecting back to our todo list page
    return redirect('todolist')

# Ensuring that only a logged in user gets to see the list of tasks
@login_required
# Method to update pending tasks with
def pending_task(request,task_id):
    """This view takes in a task id and deletes the task corresponding to the id
    """
    # Getting our task from the database
    task = TaskMate.objects.get(pk=task_id)
    # Updating the done field to true
    task.done = False
    task.save()

    # Redirecting back to our todo list page
    return redirect('todolist')

# Ensuring that only a logged in user gets to see the list of tasks
@login_required
# Method to delete tasks with
def delete_task(request,task_id):
    """This view takes in a task id and deletes the task corresponding to the id
    """
    # Getting our task from the database
    task = TaskMate.objects.get(pk=task_id)
    # Deleting the task
    task.delete()

    # Redirecting back to our todo list page
    return redirect('todolist')

def contact(request):
    """This view takes a request from a user and returns a httpresponse
    """
    # A dictionary of responses
    context = {
                'contact_text':"Welcome to Contact Page."
              
              }
    # return HttpResponse('Website is Live!')
    return render(request, 'contact.html', context)

def about(request):
    """This view takes a request from a user and returns a httpresponse
    """
    # A dictionary of responses
    context = {
                'about_text':"Welcome to About Us page."
              
              }
    # return HttpResponse('Website is Live!')
    return render(request, 'aboutUs.html', context)

