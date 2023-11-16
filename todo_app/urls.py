from django.urls import path
from .views import TaskListCreateView, TaskDetailView, IndexView, CreateGoogleDriveDocument

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('create-document/', CreateGoogleDriveDocument.as_view(), name='create-document'),
    path('', IndexView.as_view(), name='index'),
]