from rest_framework.viewsets import ModelViewSet
# Create your views here.
from .models import Note
from .serializer import NoteSerializer

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
