from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UzdrowiskoViewSet

Uzdrowisko_router = DefaultRouter()
Uzdrowisko_router.register(r'uzdrowisko',UzdrowiskoViewSet)