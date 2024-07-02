from urllib import request
import re
import json



# Get Public IP

def getPublicIP():
    data = str(request.urlopen('http://checkip.dyndns.com/').read())
    return re.compile(r'Address: (\d+.\d+.\d+.\d+)').search(data).group(1)

IP = str(getPublicIP())
# print(IP)


# Get Location

def getLocation(IP):
    url = 'http://ip-api.com/json/' + IP
    response = request.urlopen(url)
    data = json.load(response)
    city = data['city']
    return(city)

city = getLocation(IP)
# print(city)


# Get Weather

response = request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=92ab07ffc1983bd425df44e2c4ae0c18')
data = json.load(response)

print(f"Your City : {data['name']}")
print(f"Weather   : {data['weather'][0]['main']}")
print(f"Temp      : {str(int(data['main']['temp'] - 273))}C")
print(f"Humidity  : {data['main']['humidity']}%")





# api key = &appid=92ab07ffc1983bd425df44e2c4ae0c18
# untuk dapat api key , daftar dolo di openweathermap.org
