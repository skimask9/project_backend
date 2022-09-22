from django.contrib import admin
from django.urls import path
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet


schema_view = get_swagger_view(title="Two DEMO API")
router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("swagger/", schema_view),
] + router.urls
