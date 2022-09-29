from django.db import models
from core.models import BaseModel


class Video(BaseModel):
    title = models.CharField(max_length=255, default="no title")
    url = models.URLField(max_length=255)

    def __str__(self):
        return self.title
