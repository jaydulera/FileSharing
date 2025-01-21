from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import File
from .serializers import FileSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return File.objects.filter(owner=self.request.user) | File.objects.filter(shared_with=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)