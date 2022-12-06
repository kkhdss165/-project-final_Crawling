#지하철 승하차 크롤링

import urllib.request
import json


service_url = "http://openapi.seoul.go.kr:8088/63506f52766b6b68313033657a4a6367/json/CardSubwayTime/1/5/202111/"

print(service_url)
req = urllib.request.Request(service_url)
response = urllib.request.urlopen(req)
decodeData = response.read().decode('utf-8')
jsonData = json.loads(decodeData)


print(jsonData)