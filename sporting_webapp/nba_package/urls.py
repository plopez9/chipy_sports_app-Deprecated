from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("json_summary", views.summary_request, name="summary_request"),
    path("json_player", views.player_request, name="player_request"),
]
