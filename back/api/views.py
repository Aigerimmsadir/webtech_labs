from django.http import JsonResponse
from api.models import TaskList,Task


def task_list(request):
    lists = TaskList.objects.all()
    json_categories = [l.to_json() for l in lists]
    return JsonResponse(json_categories, safe=False)


def list_detail(request, pk):
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(list.to_json(),safe=False)


def list_tasks(request, pk):
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = list.tasks.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)

def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(task.to_json(),safe=False)