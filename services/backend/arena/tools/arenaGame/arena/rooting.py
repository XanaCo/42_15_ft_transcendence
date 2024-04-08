from django.urls import re_path

from . import battle

websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", battle.Challenger.as_asgi()),
]