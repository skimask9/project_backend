from ckeditor.fields import RichTextField
from core.models import BaseImage, BaseModel
from django.db import models

# Create your models here.


class Post(BaseModel):
    title = models.CharField(max_length=256, blank=True)
    body = RichTextField()

    def __str__(self):
        return f"{self.title}"


class PostImage(BaseImage):
    post_name_id = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True
    )
