from django.shortcuts import render, HttpResponse
from .models import StoreBase
# Create your views here.
def home(request):
    return render(request, "home.html")


def stadis(request):
    queryset= StoreBase.objects.all()
    return render(request, "names.html",{"names": queryset } )