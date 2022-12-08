#지하철 승하차 크롤링

import urllib.request
import json

service_url = "http://openapi.seoul.go.kr:8088/"
service_key = "63506f52766b6b68313033657a4a6367"

def get_subway_pos():
    #지하철 역 613개

    start = 1
    end = 1000

    parameters = service_key + "/"
    parameters += "json" + "/"
    parameters += "subwayStationMaster" + "/"
    parameters += str(start) + "/"
    parameters += str(end) + "/"
    parameters += "202211" + "/"

    url = service_url + parameters
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    decodeData = response.read().decode('utf-8')
    jsonData = json.loads(decodeData)

    # print(jsonData)
    #
    # req_CODE = jsonData['subwayStationMaster']['RESULT']['CODE']
    #
    # print(req_CODE)
    #
    # if req_CODE == 'INFO-000':
    #     subways = jsonData['subwayStationMaster']['row']
    #     for subway in subways:
    #         print(subway)
    #
    # print(len(subways))

    return jsonData

get_subway_pos()