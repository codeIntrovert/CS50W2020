from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def say_hello(request):
    url = "https://api.alquran.cloud/v1/ayah/1/en.asad"
    response = requests.get(url)
    json_response = response.json()
# Extract the "text" field from the JSON data
    text = json_response["data"]["text"]

    return render(request, 'index.html',{'ayat':text})
