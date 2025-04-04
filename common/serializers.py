from rest_framework import serializers
from .models import File

class FileUploadSerialized(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['id', 'file', 'resource_type']