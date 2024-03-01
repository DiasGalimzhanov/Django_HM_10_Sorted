from django.shortcuts import render
from .models import CustomUser, Todo
from django.db.models import Avg

def home(request):
    users = CustomUser.objects.all()
    return render(request, 'home.html', {'users': users})

def todos(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request, 'todos.html', {'todos': user.todos.all()})

def todos_by_status(request, status):
    todos = Todo.objects.filter(status=status)
    return render(request, 'todos_by_status.html', {'todos': todos, 'status': status})

def values(request):
    values = Todo.objects.values('status', 'deadline', 'title')
    return render(request, 'values.html', {'values': values})

def exludes(request):
    exludes = CustomUser.objects.exclude(gender=CustomUser.GenderChoices.M)
    return render(request, 'exludes.html', {'exludes': exludes})

def exludes_f(request):
    exludes = CustomUser.objects.exclude(gender=CustomUser.GenderChoices.F)
    return render(request, 'exludes_f.html', {'exludes': exludes})