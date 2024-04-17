# link with urls.py
from django.urls import path

# get views.py file
from . import views

from .views import testView

urlpatterns = [
	path("", views.index, name="index"),
	path("", views.runGames, name="runGames"),
	path('testView/', testView, name='testView'),
]
