from django.contrib import admin

# Register your models here.
from .models import PlayerInfo, SummaryStats, Contracts

admin.site.register(PlayerInfo)

admin.site.register(SummaryStats)

admin.site.register(Contracts)
