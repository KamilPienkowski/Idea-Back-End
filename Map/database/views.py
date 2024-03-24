from django.shortcuts import render
from django.http import HttpResponse
from database.uzdrowisko import Uzdrowisko
from ai import AiTool
# Create your views here.

uzdrowisko = Uzdrowisko()
chat  = AiTool()
def index(request):
    return render(request,'index.html')

def search(request):
    key = request.GET['key']
    znalezione = uzdrowisko.search_in_xlsx(key)
    return render(request,'search.html',{'list' : zip(znalezione[0],znalezione[1])})