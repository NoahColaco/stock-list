from django.http import HttpResponse
import requests


def returnStock(request):  

    url = "https://finnhub.io/api/v1/search?q=tesla"

    response = requests.request("GET", url, params=headers)

    return HttpResponse(response)

def index(request):
    return HttpResponse("Hi Sinan")