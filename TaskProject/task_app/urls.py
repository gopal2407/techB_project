from django.urls import path
from .views import task, task_details, search_by_id, add_task, delete_task, edit_task, mark_task, search_by_task


urlpatterns = [
    path('task/', task),
    path('task/<int:pk>/', task_details),
    path('task/search/<int:pk>/', search_by_id),
    path('add/', add_task),
    path('delete/<int:pk>/', delete_task),
    path('edit/<int:pk>/', edit_task),
    path('mark/<int:pk>/', mark_task),
    path('task/search/<str:pk>/', search_by_task)
]