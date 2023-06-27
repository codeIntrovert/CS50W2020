from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.

def quranAPI(request):
    url = "https://api.alquran.cloud/v1/ayah/1/en.asad"
    response = requests.get(url)
    json_response = response.json()
    text = json_response["data"]["text"]
    surahName = json_response['data']['surah']['englishName']
    return render(request, 'index.html',{'ayatHtml':text, 'surahNameHtml': surahName})

def showIndex(request):
    return render(request, 'index.html',{'ayatHtml': 'This Route has been set perfectly'})

