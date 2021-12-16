""" The endpoint of the APP.

"""
from django.urls import path
from . import views

urlpatterns = [
    path('api/v1', views.api)
]
