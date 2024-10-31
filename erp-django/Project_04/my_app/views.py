from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Project
from config.serializers import ProjectSerializer

# Create your views here.

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
