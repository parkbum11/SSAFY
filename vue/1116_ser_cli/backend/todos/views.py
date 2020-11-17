from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.
@api_view(['GET', 'POST'])
# 도착한 토큰이 정상인지 # 정상이면 request에 user 객체를 넣어줌
@authentication_classes([JSONWebTokenAuthentication]) 
# token 유무 검사
@permission_classes([IsAuthenticated]) 
def todo_list_create(request):
    if request.method == 'GET':
        # todo database에서 todo 정보를 모두 긁어서 JSON응답
        # model => QuerySet => dict, string => JSON응답
        serializer = TodoSerializer(request.user.todos, many=True)
        return Response(serializer.data)
    else:
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)


@authentication_classes([JSONWebTokenAuthentication]) 
@permission_classes([IsAuthenticated]) 
@api_view(['PUT','DELETE'])
def todo_update_delete(request, todo_id):
    todo=get_object_or_404(Todo, pk=todo_id)
    if request.method=='PUT':
        serializer=TodoSerializer(instance=todo,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    else:
        todo.delete()
        return Response({'id':todo_id})