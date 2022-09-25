from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class VideoApiView(APIView):
    def get(self, request):
        return Response({"message": True, "videos": [],"status":status.HTTP_200_OK}, status.HTTP_200_OK)
