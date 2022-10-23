from django.contrib import admin
from .models import Host, Player, Tournament

# Register your models here.
admin.site.register(Host)
admin.site.register(Player)
admin.site.register(Tournament)