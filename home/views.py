from django.shortcuts import render
from todo.models import Todo
from django.http import HttpRequest, JsonResponse

def index_page(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'home/index.html', context)

def todo_json(request: HttpRequest):
    todos = list(Todo.objects.all().values('title', 'is_done'))
    return JsonResponse({'todos': todos})