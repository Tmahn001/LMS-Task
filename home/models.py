from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.conf import settings
import uuid

# Create your models here.
status_data = (('Open', 'Open'), ('Pending', 'Pending'), ('Completed', 'Completed'))
class LeadManagement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=125)
    mobile_number = models.CharField(max_length=50, null=True)
    status = models.CharField(max_length=100, choices=status_data)
    address = models.TextField()
    industry = models.CharField(max_length=125)
    website = models.URLField(max_length=200)
    contacts = models.CharField(max_length=126)
    pipelines = models.TextField()
    notes = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='customer')
    def __str__(self):
        return self.name

