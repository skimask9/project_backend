from django.db import models
from core.models import BaseModel


class Note(BaseModel):
    title = models.CharField(max_length=110)
    content = models.TextField()

    def __str__(self):
        return self.title
