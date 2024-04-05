import requests
from django.shortcuts import render
from rest_framework import generics
from .models import Match
from .serializers import MatchSerializer
# Create your views here.



class MatchList(generics.ListAPIView):
    queryset=Match.objects.all()
    serializer_class= MatchSerializer

    

def fetch_match_data(request):
    headers = {
        'X-RapidAPI-Key': "b8518d38b7mshf201699e0d6ff6dp1643e2jsna49b470d1285",
        'X-RapidAPI-Host': "sport-highlights-api.p.rapidapi.co"
    }

    api_url="https://sport-highlights-api.p.rapidapi.com/football/countries/FR"


    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        # Process the data and save it to your database
        for match_data in data:
            home_team = match_data.get('home_team')
            away_team = match_data.get('away_team')
            match_date = match_data.get('match_date')


            match = Match(home_team=home_team, away_team=away_team, match_date=match_date)
            match.save()

        return render(request, 'result/success.html')
    else:
        return render(request, 'result/error.html', {'error': response.status_code})

            

           