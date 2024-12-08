from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404

class TodoAPI(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request, pk=None):
        if pk:  
            todo = get_object_or_404(Todo, pk=pk)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: 
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)  
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.delete()
        return Response({"message": "Todo deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)
        