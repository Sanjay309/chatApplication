from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/jwc/<str:groupname>/', consumers.MyJsonWebsocketConsumer.as_asgi()),
]