from rest_framework.viewsets import ModelViewSet
from .serializers import UzdrowiskoSelializer
from ..models import Uzdrowisko

class UzdrowiskoViewSet(ModelViewSet):
    queryset = Uzdrowisko.objects.all()
    serializer_class = UzdrowiskoSelializer


