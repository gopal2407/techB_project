from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer
from .models import Task
from django.shortcuts import get_object_or_404


# Create your views here.


@api_view(http_method_names=['GET'])
def search_by_id(request, pk):
    objects = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        serializer = TaskSerializer(objects)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(data={'message': 'Task with this id is not available'}, status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['POST'])
def add_task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=400)


@api_view(http_method_names=['DELETE'])
def delete_task(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    if request.method == 'DELETE':
        obj.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=['PUT', 'PATCH'])
def edit_task(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    if request.method == 'PUT':
        serializer = TaskSerializer(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=400)
    if request.method == 'PATCH':
        serializer = TaskSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=400)


@api_view(http_method_names=['PATCH'])
def mark_task(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    if request.method == 'PATCH':
        serializer = TaskSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=400)


# CRUD Not a part of project
@api_view(http_method_names=['GET', 'POST'])
def task(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=400)
    objs = Task.objects.all()
    serializer = TaskSerializer(objs, many=True)
    return Response(data=serializer.data, status=200)


@api_view(http_method_names=['GET', 'PUT', 'PATCH', 'DELETE'])
def task_details(request, pk):
    obj = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        serializer = TaskSerializer(obj)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = TaskSerializer(data=request.data, instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=400)
    if request.method == 'PATCH':
        serializer = TaskSerializer(data=request.data, instance=obj, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(data=serializer.errors, status=400)
    if request.method == 'DELETE':
        obj.delete()
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)
