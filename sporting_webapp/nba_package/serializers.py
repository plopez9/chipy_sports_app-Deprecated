from rest_framework import serializers
from .models import SummaryStats, PlayerInfo, Contracts

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerInfo
        fields = ("player", "pos", "ht", "wt", "birth_date", "exp", "college",
        "url", "year")
        read_only_fields = [f.name for f in PlayerInfo._meta.get_fields()]

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = ("player", "tm", "number_2018_19", "number_2019_20",
            "number_2020_21", "number_2021_22", "number_2022_23",
            "number_2023_24", "signed_using", "guaranteed")
        read_only_fields = [f.name for f in Contracts._meta.get_fields()]

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = SummaryStats
        fields = ("player", "tm", "g", "gs", "mp", "fg", "fga", "fg_percent",
        "number_3p", "number_3pa", "number_3p_field", "number_2p", "number_2pa",
        "number_2p_field", "efg_field", "ft", "fta", "ft_field", "orb", "drb",
        "trb", "ast", "stl", "blk", "tov", "pf", "pts", "year")
        read_only_fields = [f.name for f in SummaryStats._meta.get_fields()]
