from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("PlayerInfo", views.PlayerView)
router.register("Contracts", views.ContractView)
router.register("Summary", views.SummaryView)

urlpatterns = [
    path('', views.index, name='index'),
    path("json", include(router.urls)),
    path("home", views.home_screen, name="Home Screen")
#    path("json_summary", views.summary_request, name="summary_request"),
#    path("json_player", views.player_request, name="player_request"),
#    path("json_contracts", views.contract_request, name="contract_request")

]
