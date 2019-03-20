from django.shortcuts import render
from django.http import HttpResponse

from .models import SummaryStats as st
from .models import PlayerInfo as pi
from .models import Contracts as c

from .serializers import PlayerSerializer, ContractSerializer, SummarySerializer

from rest_framework import viewsets
from django.core.serializers import serialize


# Create your views here.
def index(request):
    return render(request, "nba_package/first_screen.html")

#def summary_request(request):
#    response = serialize("json", st.objects.all())
#    return HttpResponse(response, content_type="application/json")

#def player_request(request):
#    response= serialize("json", pi.objects.all())
#    return HttpResponse(response, content_type="application/json")

#def contract_request(request):
#    response = serialize("json", c.objects.all())
#    return HttpResponse(response, content_type="application/json")

class PlayerView(viewsets.ModelViewSet):
    queryset = pi.objects.all()
    serializer_class = PlayerSerializer

class ContractView(viewsets.ModelViewSet):
    queryset = c.objects.all()
    serializer_class = ContractSerializer

class SummaryView(viewsets.ModelViewSet):
    queryset = st.objects.all()
    serializer_class = SummarySerializer
