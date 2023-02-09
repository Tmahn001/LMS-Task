from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
import logging
from rest_framework.views import APIView



import base64


from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import LeadManagement
from .serializer import LeadSerializer, LeadOutputSerializer
from .tasks import read_csv_data
from .validator import check_time
import json
from rest_framework import generics
import pandas as pd

from .forms import ImportForm, LeadForm

from rest_framework import status
from rest_framework.response import Response

from .models import LeadManagement


class LMSView(viewsets.ViewSet):
    def create(self, request):
        
        data = request.FILES.get("file")
        data = base64.b64encode(data.read()).decode("utf-8")
        task = read_csv_data.delay(data)
        return Response(
            {
                "status": task.status,
                "message": "uploading to db...",
            },
            status=status.HTTP_200_OK,
        )
class LeadsView(APIView):
    def get(self, request):
        if request.method=='GET':
            lead_data = LeadManagement.objects.all()
            lead_data_serializer= LeadOutputSerializer(lead_data, many=True)

            return Response(lead_data_serializer.data

    )


