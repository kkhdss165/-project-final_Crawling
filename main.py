#지하철 승하차 크롤링

import urllib.request
import json


service_url = "http://openapi.seoul.go.kr:8088/63506f52766b6b68313033657a4a6367/json/CardSubwayTime/1/100/202211/"
service_url = "http://openapi.seoul.go.kr:8088/"
service_key = "63506f52766b6b68313033657a4a6367"

parameters = service_key + "/"
parameters += "json" + "/"
parameters += "CardSubwayTime" + "/"
parameters += "1" + "/"
parameters += "700" + "/"
parameters += "202211" + "/"

url = service_url + parameters

print(url)
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
decodeData = response.read().decode('utf-8')
jsonData = json.loads(decodeData)

print(jsonData)

if jsonData['CardSubwayTime']['RESULT']['CODE'] == 'INFO-000' :

    subways = jsonData['CardSubwayTime']['row']

    print(subways)

    for subway in subways:
        print(subway)

    print(len(subways))