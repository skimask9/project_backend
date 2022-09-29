# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Video
from .serializers import VideoSerializer

# class VideoApiView(APIView):
#     def get(self, request):
#         return Response(
#             {"message": True, "videos": [], "status": status.HTTP_200_OK},
#             status.HTTP_200_OK,
#         )


class VideoViewSet(ReadOnlyModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
