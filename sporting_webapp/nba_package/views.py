from django.shortcuts import render
from django.http import HttpResponse

from .models import SummaryStats as st
from .models import PlayerInfo as pi
from .models import Contracts as c

from django.core.serializers import serialize


# Create your views here.
def index(request):
    return render(request, "nba_package/first_screen.html")

def summary_request(request):
    response = serialize("json", st.objects.all())
    return HttpResponse(response, content_type="application/json")

def player_request(request):
    response= serialize("json", pi.objects.all())
    return HttpResponse(response, content_type="application/json")

def contract_request(request):
    response = serialize("json", c.objects.all())
    return HttpResponse(response, content_type="application/json")
