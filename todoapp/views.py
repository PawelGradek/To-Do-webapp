from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse,JsonResponse
import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')

def add(request):
    elem = Todo()
    elem.title = request.GET['title']
    elem.description = request.GET['description']
    elem.priority = request.GET['priority']
    elem.save()
    allelements = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list-of-all.html',context=allelements)

def delete(request,id):
    elem = Todo.objects.get(id=id)
    elem.delete()
    allelements = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list-of-all.html',context=allelements)

def listofallelems(request):
    allelements = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list-of-all.html',context=allelements)

def edit(request,id):
    elem = Todo.objects.get(id=id)
    allelements = {
        "title" : elem.title,
        "description" : elem.description,
        "priority" : elem.priority,
        "id" : elem.id
    }
    return render(request,'edit-to-do.html',context=allelements)


def update(request,id):
    elem = Todo(id=id)
    elem.title = request.GET['title']
    elem.description = request.GET['description']
    elem.priority = request.GET['priority']
    timeis = datetime.datetime.now()
    elem.created_at = timeis
    elem.save()
    allelements = {
        "alltodos" : Todo.objects.all()
    }
    return render(request,'list-of-all.html',context=allelements)
