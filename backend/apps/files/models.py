from django.db import models
from core.models import BaseModel


class File(BaseModel):
    file = models.FileField(upload_to="files")
    title = models.CharField(max_length=255, default="No Title")

    def __str__(self):
        return self.title
