from django.forms import FileField, Form, ModelForm

from .models import LeadManagement


class LeadForm(ModelForm):
    class Meta:
        model = LeadManagement
        fields = ["name", "mobile_number", "status","address", "industry", "website","pipelines", "notes"]


class ImportForm(Form):
    products_file = FileField()

