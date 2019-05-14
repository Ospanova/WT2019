from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer


@csrf_exempt
def task_lists(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)

@csrf_exempt
def task_list_details(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskListSerializer(task_list, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)

    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({}, status=204)


@csrf_exempt
def task_list_tasks(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        tasks = task_list.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)


@csrf_exempt
def task_details(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = TaskSerializer(instance=task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors)

    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({}, status=204)
