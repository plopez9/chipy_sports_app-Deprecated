from django.contrib import admin

# Register your models here.
from .models import PlayerInfo, SummaryStats

admin.site.register(PlayerInfo)

admin.site.register(SummaryStats)
