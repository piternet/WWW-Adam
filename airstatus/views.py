import requests
import json
from django.shortcuts import redirect
from django.urls import reverse
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
        return redirect('%s%s?name=' % (reverse('aircountry'),countrycode)+a)
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

def aircity(request, country, **kwargs):
    countryname = request.GET['name']
    oururl = "https://api.openaq.org/v1/cities"
    r = requests.get(oururl + "?country="+country)
    jdata = r.text
    results = json.loads(jdata)['results']
    if request.method == "POST":
        a = request.POST['drop1']
        print(a)
        return HttpResponseRedirect(a + "?name=" + countryname)
    else:
        cityonly = []
        for ct in results:
            for k, v in ct.items():
                if k == 'city':
                    cityonly.append(v)
        context = {
            'cityonly': cityonly,
            'countryname': countryname
        }
        return render(request, 'main/air_city.html', context)


def airlocation(request, country, city, **kwargs):
    countryname = request.GET['name']
    oururl = "https://api.openaq.org/v1/latest"
    r = requests.get(oururl + "?country=" + country + "&city=" + city)
    jdata = r.text
    results = json.loads(jdata)['results']
    if request.method == "POST":
        a = request.POST['drop1']
        print(a)
        return HttpResponseRedirect('asdf')
    else:
        locationonly = []
        context = {
            'locationonly': locationonly,
            'countryname': countryname
        }
        return render(request, 'main/air_city.html', context)