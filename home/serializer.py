from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import LeadManagement
class LeadSerializer(ModelSerializer):
    class Meta:
        model = LeadManagement
        fields = "__all__"


class FileUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    class Meta:
        fields = ("file",)