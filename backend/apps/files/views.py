from rest_framework import viewsets
from .models import File

from .serializers import FileSerializer
from core.permissions import IsSubscriber
# Create your views here.


class FileViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
    permission_classes = [IsSubscriber]
