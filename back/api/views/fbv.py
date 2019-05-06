from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskSerializer
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
@api_view(['GET','POST'])
@csrf_exempt
@permission_classes((IsAuthenticated, ))
def task_list_list(request):
    permission_classes = (IsAuthenticated,)
    if request.method == 'GET':

        tasks_list = TaskList.objects.all()
        serializer = TaskListSerializer(tasks_list, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    elif request.method == 'POST':

        serializer = TaskListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})


@csrf_exempt
def task_list_detail(request, pk):
    permission_classes = (IsAuthenticated,)
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=404)

    if request.method == 'GET':
        serializer = TaskListSerializer(task_list)
        return JsonResponse(serializer.data, status=200)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer(instance=task_list, data=body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        task_list.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})


def task_list_tasks(request, pk):
    permission_classes = (IsAuthenticated,)
    try:
        task_list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=404)

    tasks = task_list.task_set.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False, status=200)


