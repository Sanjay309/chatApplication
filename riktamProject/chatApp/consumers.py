from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
from django.contrib.auth.models import Group, User
from .models import Chat

class MyJsonWebsocketConsumer(JsonWebsocketConsumer):
    def connect(self):
        print("websocket connected...")
        self.group_name = self.scope['url_route']['kwargs']['groupname']
        print("group_name", self.group_name)
        print("channel_name", self.channel_name)
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def receive_json(self, content, **kwargs):
        print("message received from clent....", content)
        group =Group.objects.get(name = self.group_name)

        chat = Chat(
            content = content['msg'],
            group = group,
            user = self.scope['user']
        )
        chat.save()
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type' : 'chat.message',
                'message': content['msg']
            }
        )

    def disconnect(self, close_code):
        print("websocket disconnected...", close_code)
    
    def chat_message(self, event):
        print("Event..", event)
        self.send_json({
            'message': event['message']
        })
