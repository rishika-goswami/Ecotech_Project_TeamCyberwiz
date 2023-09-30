import csv
import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import ctypes

def deforestation(index):
    url="https://www.globalforestwatch.org/dashboards/country/IND/" + index
    page=requests.get(url)
    s=page.text
    index=s.find('div class="description text -title-xs"')
    index2=s.find('class="c-subnav-menu theme-subnav-dark nav')
    text=s[index+135:index2-1229]

    text=text.split("<b>")

    temp=""
    for i in text:
        temp+=i
    text=temp
    text=text.split("</b>")
    temp=""
    for i in text:
        temp+=i
    text=temp
    text=text.split("&lt; ")
    temp=""
    for i in text:
        temp+=i
    
    WS_EX_TOPMOST=0x40000
    windowTitle="Deforestation Data"
    message=temp
    ctypes.windll.user32.MessageBoxExW(None,message,windowTitle,WS_EX_TOPMOST)   

def temperature(city_name):
    geolocator = Nominatim(user_agent="MyApp")
    n=city_name
    location = geolocator.geocode(n)

    print("The latitude of the location is: ", location.latitude)
    print("The longitude of the location is: ", location.longitude)
    latitude=str(location.latitude)
    longitude=str(location.longitude)
    url="https://www.ventusky.com/"+latitude+";"+longitude    

    page=requests.get(url)    
    s=page.text
    temp_index=s.find('class="temperature"')
    temp_f=s[temp_index+46:temp_index+48]
    return [n,temp_f]
    print("The temperature in {} is {} F.".format(n,temp_f))  

def airpressure(city_name):
    geolocator = Nominatim(user_agent="MyApp")
    n=city_name
    location = geolocator.geocode(n)

    print("The latitude of the location is: ", location.latitude)
    print("The longitude of the location is: ", location.longitude)
    latitude=str(location.latitude)
    longitude=str(location.longitude)
    url="https://www.ventusky.com/"+latitude+";"+longitude    

    page=requests.get(url)    
    s=page.text
    
    air_p_index=s.find('hPa')
    air_p_index_f=s[air_p_index-7:air_p_index-1]
    while(True):
        if(air_p_index_f[-1].isdigit() == False):
            air_p_index_f=air_p_index_f[:len(air_p_index_f)-1]
        else:
            break
    while(True):
        if(air_p_index_f[0].isdigit() == False):
            air_p_index_f=air_p_index_f[1:]
        else:
            break
    return [n,air_p_index_f] 
