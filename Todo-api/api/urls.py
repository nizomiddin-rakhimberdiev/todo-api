from django.urls import path

from api import views

urlpatterns = [
    path('todos/', views.TodoListAPIView.as_view(), name='todo-list'),
    path('create/', views.CreateTodoApiView.as_view(), name='create'),
    path('todos/<int:id>/', views.TodoDetailApiView.as_view(), name='detail')
]

