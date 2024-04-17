from django.urls import re_path

from . import battle

websocket_urlpatterns = [
    re_path(r"ws/challenger/$", battle.Challenger.as_asgi()),
]