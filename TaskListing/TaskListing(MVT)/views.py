# views.py - Handels request, retrieves data, renders template
from django.shortcuts import render
from .models import TaskListing
def task_list_view(request):
    # 1.Interact with the Model:Fetch all Task objects from the database
    all_task=TaskListing.objects.all()
    # 2.Prepare the Context:A dictionary to pass data to template
    context={
        'task':all_task,
        'tittle':'MVT Task List'
    }