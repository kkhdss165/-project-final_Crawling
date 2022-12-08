#지하철 승하차 크롤링

import urllib.request
import json
import re

service_url = "http://openapi.seoul.go.kr:8088/"
service_key = "63506f52766b6b68313033657a4a6367"

def get_subway_data():
    result = []
    check = []
    #지하철 역 613개

    start = 1
    end = 1000

    parameters = service_key + "/"
    parameters += "json" + "/"
    parameters += "CardSubwayTime" + "/"
    parameters += str(start) + "/"
    parameters += str(end) + "/"
    parameters += "202211" + "/"



    url = service_url + parameters
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    decodeData = response.read().decode('utf-8')
    jsonData = json.loads(decodeData)



    req_CODE = jsonData['CardSubwayTime']['RESULT']['CODE']

    print(req_CODE)

    if req_CODE == 'INFO-000':
        subways = jsonData['CardSubwayTime']['row']
        for subway in subways:
            print(subway)

            sub_name = subway['SUB_STA_NM']
            sub_name = re.sub("\(.*\)|\s-\s.*","",sub_name)

            n_4 = subway['FOUR_RIDE_NUM'] + subway['FOUR_ALIGHT_NUM']
            n_5 = subway['FIVE_RIDE_NUM'] + subway['FIVE_ALIGHT_NUM']
            n_6 = subway['SIX_RIDE_NUM'] + subway['SIX_ALIGHT_NUM']
            n_7 = subway['SEVEN_RIDE_NUM'] + subway['SEVEN_ALIGHT_NUM']
            n_8 = subway['EIGHT_RIDE_NUM'] + subway['EIGHT_ALIGHT_NUM']
            n_9 = subway['NINE_RIDE_NUM'] + subway['NINE_ALIGHT_NUM']
            n_10 = subway['TEN_RIDE_NUM'] + subway['TEN_ALIGHT_NUM']
            n_11 = subway['ELEVEN_RIDE_NUM'] + subway['ELEVEN_ALIGHT_NUM']
            n_12 = subway['TWELVE_RIDE_NUM'] + subway['TWELVE_ALIGHT_NUM']
            n_13 = subway['THIRTEEN_RIDE_NUM'] + subway['THIRTEEN_ALIGHT_NUM']
            n_14 = subway['FOURTEEN_RIDE_NUM'] + subway['FOURTEEN_ALIGHT_NUM']
            n_15 = subway['FIFTEEN_RIDE_NUM'] + subway['FIFTEEN_ALIGHT_NUM']
            n_16 = subway['SIXTEEN_RIDE_NUM'] + subway['SIXTEEN_ALIGHT_NUM']
            n_17 = subway['SEVENTEEN_RIDE_NUM'] + subway['SEVENTEEN_ALIGHT_NUM']
            n_18 = subway['EIGHTEEN_RIDE_NUM'] + subway['EIGHTEEN_ALIGHT_NUM']
            n_19 = subway['NINETEEN_RIDE_NUM'] + subway['NINETEEN_ALIGHT_NUM']
            n_20 = subway['TWENTY_RIDE_NUM'] + subway['TWENTY_ALIGHT_NUM']
            n_21 = subway['TWENTY_ONE_RIDE_NUM'] + subway['TWENTY_ONE_ALIGHT_NUM']
            n_22 = subway['TWENTY_TWO_RIDE_NUM'] + subway['TWENTY_TWO_ALIGHT_NUM']
            n_23 = subway['TWENTY_THREE_RIDE_NUM'] + subway['TWENTY_THREE_ALIGHT_NUM']
            n_24 = subway['MIDNIGHT_RIDE_NUM'] + subway['MIDNIGHT_ALIGHT_NUM']
            n_1 = subway['ONE_RIDE_NUM'] + subway['ONE_ALIGHT_NUM']
            n_2 = subway['TWO_RIDE_NUM'] + subway['TWO_ALIGHT_NUM']
            n_3 = subway['THREE_RIDE_NUM'] + subway['THREE_ALIGHT_NUM']


            if sub_name not in check:
                result.append({'sub_name' : sub_name , 'n_4' : n_4, 'n_5' : n_5, 'n_6' : n_6, 'n_7' : n_7, 'n_8' : n_8, 'n_9' : n_9, 'n_10' : n_10, 'n_11' : n_11,
                               'n_12' : n_12, 'n_13' : n_13, 'n_14' : n_14, 'n_15' : n_15, 'n_16' : n_16, 'n_17' : n_17, 'n_18' : n_18, 'n_19' : n_19,
                               'n_20' : n_20, 'n_21' : n_21, 'n_22' : n_22, 'n_23' : n_23, 'n_24' : n_24, 'n_1' : n_1, 'n_2' : n_2, 'n_3' : n_3})
                check.append(sub_name)

            ## 중복 : 환승역
            else:
                for res in result:
                    if res['sub_name'] == sub_name:
                        # print(res)
                        res['n_4'] += n_4
                        res['n_5'] += n_5
                        res['n_6'] += n_6
                        res['n_7'] += n_7
                        res['n_8'] += n_8
                        res['n_9'] += n_9
                        res['n_10'] += n_10
                        res['n_11'] += n_11
                        res['n_12'] += n_12
                        res['n_13'] += n_13
                        res['n_14'] += n_14
                        res['n_15'] += n_15
                        res['n_16'] += n_16
                        res['n_17'] += n_17
                        res['n_18'] += n_18
                        res['n_19'] += n_19
                        res['n_20'] += n_20
                        res['n_21'] += n_21
                        res['n_22'] += n_22
                        res['n_23'] += n_23
                        res['n_24'] += n_24
                        res['n_1'] += n_1
                        res['n_2'] += n_2
                        res['n_3'] += n_3


    print(len(result))
    return result

subway_list = get_subway_data()

for subway in subway_list:
    print(subway)