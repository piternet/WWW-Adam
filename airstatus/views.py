import requests
import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main.models import Post, Tag, Comment, Profile, Message
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def aircountry(request):
    oururl = "https://api.openaq.org/v1/countries"
    r = requests.get(oururl + "?limit=10000")
    jdata = r.text
    results = json.loads(jdata)['results']
    if request.method == "POST":
        a = request.POST['drop1']
        for kr in results:
            for k, v in kr.items():
                if k == 'name' and v == a:
                    countrycode = kr['code']
        return HttpResponseRedirect(countrycode)
    else:
        countryonly = []
        for kr in results:
            for k, v in kr.items():
                if k == 'name':
                    countryonly.append(v)
        context = {
            'countryonly': countryonly
        }
        return render(request, 'main/air_country.html', context)

def aircity(request, country):
    oururl = "https://api.openaq.org/v1/cities"
    r = requests.get(oururl + "?country="+country)
    jdata = r.text
    results = json.loads(jdata)['results']
    print(results)
    if request.method == "POST":
        a = request.POST['drop1']
        for kr in results:
            for k, v in kr.items():
                if k == 'city' and v == a:
                    countrycode = kr['code']
        return HttpResponseRedirect(countrycode)
    else:
        cityonly = []
        for kr in results:
            for k, v in kr.items():
                if k == 'city':
                    cityonly.append(v)
        context = {
            'cityonly': cityonly
        }
        return render(request, 'main/air_city.html', context)
