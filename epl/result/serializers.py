from rest_framework import serializers
from .models import Match

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Match
        field=["id", "home_team", "away_team", "date"]