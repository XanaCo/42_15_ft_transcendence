# link with urls.py
from django.urls import path

# get views.py file
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("", views.runGames, name="runGames"),
]
