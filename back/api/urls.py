from django.urls import path
from . import views

urlpatterns = [
    path('task_lists/', views.task_list_list),
    path('task_lists/<int:pk>/', views.task_list_detail),
    path('task_lists/<int:pk>/tasks/', views.TaskListTasks.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.UserCreate.as_view()),

]