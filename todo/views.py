from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from drf_spectacular.utils import extend_schema

# @api_view(['GET'])
# def all_todos(request: Request):
#     todos = Todo.objects.all()
#     todo_serializer = TodoSerializer(todos, many=True)
#     return Response(todo_serializer.data, status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(None, status.HTTP_400_BAD_REQUEST)


class TodosListApiView(APIView):
    @extend_schema(
        request=TodoSerializer,
        responses={200: TodoSerializer},
        description='Get the list of all todos.'
    )
    def get(self, request: Request):
        todos = Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        return Response(todo_serializer.data, status.HTTP_200_OK)

    @extend_schema(
        request=TodoSerializer,
        responses={201: TodoSerializer},
        description='Create a new todo.'
    )
    def post(self, request: Request):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(None, status.HTTP_400_BAD_REQUEST)
