from django.shortcuts import render
from rest_framework import views, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from api.serializers import TodoSerializer
from todo.models import Todo


# Create your views here.

class TodoListAPIView(views.APIView):
    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)


class CreateTodoApiView(views.APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            todo = Todo.objects.create(**serializer.validated_data)
            return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetailApiView(views.APIView):
    def get(self, request, id):
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
