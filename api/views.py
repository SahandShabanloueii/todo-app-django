from django.shortcuts import render
from django.http import JsonResponse
from task.models import TodoTask
from task.models import Category
from .serializers import TodoTaskSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def todo_list(request):

    if request.method == 'GET':
        tasks = TodoTask.objects.all()
        serializer = TodoTaskSerializer(tasks, many=True)
        return JsonResponse({'Tasks':serializer.data})

    if request.method == 'POST':
        serializer = TodoTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Task added successfully!'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id):

    try:
        task = TodoTask.objects.get(pk=id)
    except TodoTask.DoesNotExist:
        return JsonResponse({'message': 'Task does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodoTaskSerializer(task)
        return JsonResponse({'Task':serializer.data})

    if request.method == 'PUT':
        serializer = TodoTaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Task updated successfully!'}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def category_list(request):

    if request.method == 'GET': 
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return JsonResponse({'Categories':serializer.data})

    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Category added successfully!'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, id):

    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return JsonResponse({'message': 'Category does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse({'Category':serializer.data})

    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Category updated successfully!'}, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        Category.delete()
        return JsonResponse({'message': 'Category deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)