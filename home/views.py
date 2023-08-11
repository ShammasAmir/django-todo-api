from django.shortcuts import render
from todo.models import Todo

def index_page(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'home/index.html', context)
