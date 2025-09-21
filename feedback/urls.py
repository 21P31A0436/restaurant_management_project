from django.urls import ppath
from .views import feedback_view

urlpattern = [
    path("", feedback_view, name="feedback")
]