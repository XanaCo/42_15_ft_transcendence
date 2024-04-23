# link with urls.py
from django.urls import path

# get views.py file
# from . import views

from .views import testView, index, runGames, testImage

# from .models import Image

urlpatterns = [
	path("", index, name="index"),
	path("", runGames, name="runGames"),
	path('testView/', testView, name='testView'),
	path('image/', testImage, name='image'),
]
