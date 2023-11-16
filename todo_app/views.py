from rest_framework import generics
from django.views.generic import TemplateView
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .drive_api import create_google_drive_document

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class IndexView(TemplateView):
    template_name = 'index.html'


class CreateGoogleDriveDocument(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data.get('data')
        name = request.data.get('name')

        if data is None or name is None:
            return Response({'error': 'Missing data or name parameter'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            file_id = create_google_drive_document(data, name)
            return Response({'file_id': file_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)