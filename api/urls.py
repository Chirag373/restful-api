from django.urls import path
from .views import TodoAPI

urlpatterns = [
    path("/todos", TodoAPI.as_view(), name="todo"),
    path("/todos/<int:pk>/", TodoAPI.as_view(), name="todo-delete")
]