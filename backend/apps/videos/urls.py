from django.urls import path
from .views import VideoApiView

app_name = "videos"
urlpatterns = [path("", VideoApiView.as_view())]
