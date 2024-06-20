from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('chat', views.chat_bot, name='chat'),
]