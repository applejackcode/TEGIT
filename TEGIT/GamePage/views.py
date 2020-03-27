from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()

    return render(request,
                  "GamePage/index.html",
                  {
                    'title' : "TEGIT | Team Estimation Game for IT",
                    'message' : "Let the Game Begin!",
                    'content' : " on " + now.strftime("%A, %d %B, %Y at %X")
                  }
           )
