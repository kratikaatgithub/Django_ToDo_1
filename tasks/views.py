from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import *
from .forms import *


#from django.db import models

# Create your models here.
#class Task(models.Model):
 #   title = models.CharField(max_length=200)
  #  complete = models.BooleanField(default=False)
   # created = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
     #   return self.title

#from django import forms
#from django.forms import ModelForm

#from models import *

#class TaskForm(forms.ModelForm):
 #   class Meta:
    #    model = Task
     #   fields = '__all__'


def index(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
         form = TaskForm(request.POST)
         if form.is_valid():
              form.save()
         return redirect('/')    

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html' ,context)

def updateTask(request, pk):
     task = Task.objects.get(id=pk)
     return render(request, 'tasks/update_task.html')