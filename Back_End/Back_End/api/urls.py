from rest_framework.routers import DefaultRouter
from uzdrowisko.api.urls import Uzdrowisko_router
from django.urls import path, include

router =DefaultRouter()

router.registry.extend(Uzdrowisko_router.registry)

urlpatterns = [
    path('', include(router.urls))
]