from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path("ws/pong/remote/(?P<user_id>\w+)/(?P<user_name>\w+)/$", consumers.PongRemoteConsumer.as_asgi()),
    re_path("ws/pong/local/(?P<user_id>\w+)/$", consumers.PongLocalConsumer.as_asgi()),
    # re_path("ws/pong/tournament", consumers.PongTournamentConsumer.as_asgi()),
]
