from rest_framework.serializers import ModelSerializer
from ..models import Uzdrowisko
class UzdrowiskoSelializer(ModelSerializer):
    class Meta:
        model = Uzdrowisko
        fields = ['name', 'address', 'phoneNumber', 'rating', 'link', 'positionx', 'positiony', 'image', 'details']

