from django.urls import path
from . import views


urlpatterns = [
   path("matchlists/", views.MatchList.as_view(), name="match-view-create"),
   path("fetch-matches/", views.fetch_match_data, name="fetch-matches"),
]

