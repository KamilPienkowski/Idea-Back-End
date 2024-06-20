import json
from django.core.management.base import BaseCommand
from ...models import Uzdrowisko

class Command(BaseCommand):
    help = 'Load markers data into Uzdrowisko model'

    def handle(self, *args, **kwargs):
        with open(r'D:\suntrail_v2\Back_End\uzdrowisko/markers.json', encoding= 'utf8') as f:
            markers = json.load(f)
            for marker in markers:
                Uzdrowisko.objects.create(
                    positionx=marker['position'][0],
                    positiony=marker['position'][1],
                    name=marker['name'],
                    address=marker['address'],
                    phoneNumber=marker['phoneNumber'],
                    link=marker['link'],
                    image=marker['image'],
                    rating=marker['rating']
                )
        self.stdout.write(self.style.SUCCESS('Successfully loaded markers data.'))