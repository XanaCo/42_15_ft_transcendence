from django.contrib import admin

from .models import elem , attack, species#, individual, player

# Register your models here.

admin.site.register(elem)
admin.site.register(attack)
admin.site.register(species)
# admin.site.register(individual)
# admin.site.register(player)
