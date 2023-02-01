from django.shortcuts import reverse
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
import logging


import base64


from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import LeadManagement
from .serializer import LeadSerializer
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
        if not check_time():
            return Response(
                {"message": "sorry you can not upload to server by this time"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = request.FILES.get("file")
        data = base64.b64encode(data.read()).decode("utf-8")
        task = read_csv_data(data)
        return Response(
            {
                "status": task.status,
                "message": "uploading to db...",
            },
            status=status.HTTP_200_OK,
        )



