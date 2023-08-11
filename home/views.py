from django.shortcuts import render
from todo.models import Todo
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def index_page(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'home/index.html', context)

@api_view(['GET'])
def todo_json(request: Request):
    todos = list(Todo.objects.all().values('title', 'is_done'))
    return Response({'todos': todos},status.HTTP_200_OK)