from rest_framework import viewsets, permissions
from projects.models import (Project, Brawler)
from .serializers import (ProjectSerializer, BrawlerSerializer)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

class BrawlerViewSet(viewsets.ModelViewSet):
    queryset = Brawler.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = BrawlerSerializer