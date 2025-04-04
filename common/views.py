from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import FileUploadSerialized

# Create your views here.
class FileUploadAPIView(APIView):
    def post(self, request):
        serializer = FileUploadSerialized(request.data)
        # serializer = FileUploadSerialized(data=request.data)
        if serializer.is_valid():
            file_instance = serializer.save()
            return Response({
                'id': file_instance.id,
                'url': file_instance.get_full_url(),
                'size': file_instance.bytes,
                'format': file_instance.format,
                'resource_type': file_instance.resource_type
            }, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)