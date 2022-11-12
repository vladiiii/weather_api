from xml.etree.ElementInclude import include
from django.urls import path, include

urlpatterns = [
    path("", include("weatherapp.urls")),
]
