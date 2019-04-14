from django.urls import path
from . import views

urlpatterns = [
    path('api/task_lists', views.task_list),
    path('api/task_lists/<int:pk>', views.list_detail),
    path('api/task_lists/<int:pk>/tasks', views.list_tasks),
    path('api/tasks/<int:pk>', views.task_detail),

]