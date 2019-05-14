from api.models import Task, TaskList
from api.serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class TaskListTasks(APIView):
    def get(self, request, pk):
        try:
            task_list = TaskList.objects.get(id=pk)
        except TaskList.DoesNotExist:
            raise Http404
        tasks = task_list.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TaskDetails(APIView):
    def get_object(self, pk):
        try:
            return Task.objects.get(id=pk)
        except Task.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)