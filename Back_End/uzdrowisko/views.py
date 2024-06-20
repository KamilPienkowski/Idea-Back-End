from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Uzdrowisko
from Back_End.ai import AiTool
import json
# Create your views here.

def index(request):
    return render(request,"index.html")

#Not tested yet
@csrf_exempt
def chat_bot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name_f = data.get('name')
        print(name_f)
        try:
            new_bot = AiTool()
            uzdrowisko = Uzdrowisko.objects.get(name=name_f)
            opinions = uzdrowisko.opinions.all()
            opinion_list = ""
            for n in opinions:
                opinion_list += n.text
            opinion = new_bot.GetSentiment(opinion_list)
            return JsonResponse({'opinion': opinion}, status=200)
        except:
            return JsonResponse({'error': 'Uzdrowisko not found'}, status=404)
       
    return JsonResponse({'error': 'Method not allowed'}, status=405)
