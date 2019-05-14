from api.models import TaskList
from api.serializers import TaskListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def task_lists(request):
    if request.method == 'GET':
        task_lists = TaskList.objects.all()
        serializer = TaskListSerializer(task_lists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def task_list_details(request, pk):
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return Response(status.HTTP_204_NO_CONTENT)