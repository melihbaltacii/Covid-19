import http.client
import json


from django.shortcuts import render


# Create your views here.
from pip._vendor import requests


def coviddashboard(request):

    #ip address
    url = 'http://ip-api.com/json/'
    r = requests.get(url).json()
    IPAddress = r["query"]
    city = r["city"]
    country = r["country"]
    # status = r["status"]
    # country = r["country"]
    # countryCode = r["countryCode"]
    # region = r["region"]
    # regionName = r["regionName"]
    # lat = r["lat"]
    # lon = r["lon"]



    # All Country
    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
        'content-type': "application/json",
        'authorization': "apikey 0RtruoSsdrozB9ea7njTT3:7yJq3TTeen7QCcrHeKSqYK"
    }
    conn.request("GET", "/corona/countriesData", headers=headers)
    res = conn.getresponse()
    data = res.read()
    contruyAll=json.loads(data)
    resultdata=contruyAll["result"]




    # All Data
    conn.request("GET", "/corona/totalData", headers=headers)
    resAllData = conn.getresponse()
    dataAllData = resAllData.read()
    WorldTotal = json.loads(dataAllData)
    WorldResultData = WorldTotal["result"]



    # AlphaCode2
    AlphaCode2=requests.get("https://restcountries.eu/rest/v2/all")
    code2=AlphaCode2.text
    Code2Data=json.loads(code2)


    # maps data

    thumbnail_list = []
    for Code2name in Code2Data:
        for countryname in resultdata:
            if Code2name['name'] == countryname['country']:
                mapList = {}
                mapList['alphaCode'] = Code2name['alpha2Code']
                mapList['value'] = countryname['totalCases']
                thumbnail_list.append(mapList)



    for countryname in resultdata:
        if "USA"== countryname['country']:
            mapList = {}
            mapList['alphaCode'] = "US"
            mapList['value'] = countryname['totalCases']
            thumbnail_list.append(mapList)
        if "Iran" == countryname['country']:
            mapList = {}
            mapList['alphaCode'] = "IR"
            mapList['value'] = countryname['totalCases']
            thumbnail_list.append(mapList)

        if "Russia" == countryname['country']:
            mapList = {}
            mapList['alphaCode'] = "RU"
            mapList['value'] = countryname['totalCases']
            thumbnail_list.append(mapList)

        if "Bolivia" == countryname['country']:
            mapList = {}
            mapList['alphaCode'] = "BO"
            mapList['value'] = countryname['totalCases']
            thumbnail_list.append(mapList)




   # Guest Data
    for result in resultdata:

        if country== result['country']:
            guestCountry=result['country']
            guestTotalCases = result['totalCases']
            guestNewCases = result['newCases']
            guestTotalDeaths = result['totalDeaths']
            guestNewDeaths = result['newDeaths']
            guestTotalRecovered = result['totalRecovered']
            guestActiveCases = result['activeCases']




    context={
        "resultdata": resultdata,
        "WorldResultData":WorldResultData,
        "IPAddress": IPAddress,
        "city": city,
        "country":country,
        "guestCountry":guestCountry,
        "guestTotalCases":guestTotalCases,
        "guestNewCases":guestNewCases,
        "guestTotalDeaths":guestTotalDeaths,
        "guestNewDeaths":guestNewDeaths,
        "guestTotalRecovered":guestTotalRecovered,
        "guestActiveCases":guestActiveCases,
        "Code2Data":Code2Data,
        "thumbnail_list":thumbnail_list,

    }

    return render(request,'coviddashboard.html',context=context)

