import http.client
import json


from django.shortcuts import render


# Create your views here.
from pip._vendor import requests


def coviddashboard(request):

    #ip address

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    
    url = 'http://ip-api.com/json/'+ip+''
    r = requests.get(url).json()
    
    print("URLLLLLLLLLLLLLLLLLLL"+str(url))
    
    if r["status"]=="success":
        
        if r["query"] =="":
            IPAddress = "Not Found"
        else:
            IPAddress = r["query"]
            
        if r["city"] is None:
            city="Not Found"
        else:
            city = r["city"]
    
        if r["country"] == "":
            country = "Not Found"
        else:
            country = r["country"]
    else:
        IPAddress = "Not Found"
        city = "Not Found"
        country = "Not Found"
            
    


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


    # maps data  and select Country List
    thumbnail_list = []
    selectCountryList=[]
    for Code2name in Code2Data:
        for countryname in resultdata:
            if Code2name['name'] == countryname['country']:
                mapList = {}
                mapList['alphaCode'] = Code2name['alpha2Code']
                mapList['value'] = countryname['totalCases'].replace(",","")

                selectList={}
                selectList["alphaCode"]=Code2name['alpha2Code']
                selectList["countryName"]=countryname['country']

                selectCountryList.append(selectList)
                thumbnail_list.append(mapList)



    for countryname in resultdata:
        if "USA"== countryname['country']:
            mapList = {}
            mapList['alphaCode'] = "US"
            mapList['value'] = countryname['totalCases'].replace(",","")

            selectList = {}
            selectList["alphaCode"] = Code2name['alpha2Code']
            selectList["countryName"] = countryname['country']

            selectCountryList.append(selectList)

            thumbnail_list.append(mapList)
        if "Iran" == countryname['country']:
            mapList = {}
            mapList['alphaCode'] = "IR"
            mapList['value'] = countryname['totalCases'].replace(",","")

            selectList = {}
            selectList["alphaCode"] = Code2name['alpha2Code']
            selectList["countryName"] = countryname['country']

            selectCountryList.append(selectList)

            thumbnail_list.append(mapList)

        if "Russia" == countryname['country']:
            mapList = {}
            mapList['alphaCode'] = "RU"
            mapList['value'] = countryname['totalCases'].replace(",","")

            selectList = {}
            selectList["alphaCode"] = Code2name['alpha2Code']
            selectList["countryName"] = countryname['country']

            selectCountryList.append(selectList)
            thumbnail_list.append(mapList)

        if "Bolivia" == countryname['country']:
            mapList = {}
            mapList['alphaCode'] = "BO"
            mapList['value'] = countryname['totalCases'].replace(",","")

            selectList = {}
            selectList["alphaCode"] = Code2name['alpha2Code']
            selectList["countryName"] = countryname['country']

            selectCountryList.append(selectList)
            thumbnail_list.append(mapList)


    
    print("GELEN ÜLKEEEEEEEEEE"+str(country))
    print("SAYİİİİİİİİİİİİ="+str(len(resultdata)))
   # Guest Data
    TotalResulDataNumber=len(resultdata)
    counter=0
    if country !="Not Found":
        if country=="United Kingdom":
            country="United Kingdom"
        elif country=="Unıted States":
            country="USA"

        for result in resultdata:
            counter=counter+1
            if country==result['country']:
                
                if result['totalCases']=="":
                    guestTotalCases="-"
                else:
                    guestTotalCases = result['totalCases']
                
                if result['newCases']=="":
                    guestNewCases="-"
                else:
                    guestNewCases = result['newCases']
                
                if result['totalDeaths']=="":
                    guestNewCases="-"
                else:
                    guestTotalDeaths = result['totalDeaths']
                 
                if result['newDeaths']=="":
                    guestNewDeaths="-"
                else:
                    guestNewDeaths = result['newDeaths']
                
                
                if result['totalRecovered']=="":
                    guestTotalRecovered="-"
                else:
                    guestTotalRecovered = result['totalRecovered']
                
                
                if result['activeCases']=="":
                    guestActiveCases="-"
                else:
                    guestActiveCases = result['activeCases']
            elif counter==TotalResulDataNumber:
                guestTotalCases = "-"
                guestNewCases = "-"
                guestTotalDeaths = "-"
                guestNewDeaths = "-"
                guestTotalRecovered = "-"
                guestActiveCases = "-"
                   
    else:
        guestTotalCases = "-"
        guestNewCases = "-"
        guestTotalDeaths = "-"
        guestNewDeaths = "-"
        guestTotalRecovered = "-"
        guestActiveCases = "-"


    context={
        "resultdata": resultdata,
        "WorldResultData":WorldResultData,
        "IPAddress": IPAddress,
        "city": city,
        "country":country,
        "guestTotalCases":guestTotalCases,
        "guestNewCases":guestNewCases,
        "guestTotalDeaths":guestTotalDeaths,
        "guestNewDeaths":guestNewDeaths,
        "guestTotalRecovered":guestTotalRecovered,
        "guestActiveCases":guestActiveCases,
        "Code2Data":Code2Data,
        "thumbnail_list":thumbnail_list,
        "selectCountryList":selectCountryList,

    }




    return render(request,'coviddashboard.html',context=context)

