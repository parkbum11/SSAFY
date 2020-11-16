from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def todo_list_create(request):
    if request.method == 'GET':
    # todo database에서 todo 정보를 모두 긁어서 JSON응답
    # model => QuerySet => dict, string => JSON응답
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    else:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
