from django.urls import path

from api import views

urlpatterns = [
    path('todos/', views.TodoListAPIView.as_view(), name='todo-list'),
    # path('create/', views.CreateTodoApiView.as_view(), name='create'),
    path('todos/<int:id>/', views.TodoDetailApiView.as_view(), name='detail'),

    path('', views.TodoListView.as_view(), name='list'),
    path('create/', views.TodoCreateAPIView.as_view(), name='create'),
    # path('<int:id>/', views.TodoDetailApiView.as_view(), name='detail'),
]

