from django.urls import path
from . import views
from .views import LMSView, LeadsView

urlpatterns=[
path('view', LeadsView.as_view())

]
