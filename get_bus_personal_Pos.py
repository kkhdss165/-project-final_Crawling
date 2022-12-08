## 버스 정류장별 승하차 인원정보
## 단위 월 전체

import urllib.request
import json
import re
import pandas as pd

service_url = "http://openapi.seoul.go.kr:8088/"
service_key = "63506f52766b6b68313033657a4a6367"

# 예외정류장
Exception_station = []

def get_bus_data():
    result = []
    check = []

    stations = []

    start = 1
    end = 1000

    while True:

        parameters = service_key + "/"
        parameters += "json" + "/"
        parameters += "CardBusTimeNew" + "/"
        parameters += str(start) + "/"
        parameters += str(end) + "/"
        parameters += "202211" + "/"


        url = service_url + parameters
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        decodeData = response.read().decode('utf-8')
        jsonData = json.loads(decodeData)

        # print(jsonData)
        print(url)
        try:
            req_CODE = jsonData['CardBusTimeNew']['RESULT']['CODE']

            if req_CODE == 'INFO-000':
                station_info = jsonData['CardBusTimeNew']['row']
                # print("start : ",start,"end : ",end,len(station_info))

                stations += station_info

                start += 1000
                end += 1000

            else:
                break

        except:
            break


        for station in stations:
            busst_name = station['BUS_STA_NM']
            busst_name = re.sub("\(.*\)|\s-\s.*", "", busst_name)

            if busst_name not in Exception_station:
                n_24 = station['MIDNIGHT_RIDE_NUM'] + station['MIDNIGHT_ALIGHT_NUM']
                n_1 = station['ONE_RIDE_NUM'] + station['ONE_ALIGHT_NUM']
                n_2 = station['TWO_RIDE_NUM'] + station['TWO_ALIGHT_NUM']
                n_3 = station['THREE_RIDE_NUM'] + station['THREE_ALIGHT_NUM']
                n_4 = station['FOUR_RIDE_NUM'] + station['FOUR_ALIGHT_NUM']
                n_5 = station['FIVE_RIDE_NUM'] + station['FIVE_ALIGHT_NUM']
                n_6 = station['SIX_RIDE_NUM'] + station['SIX_ALIGHT_NUM']
                n_7 = station['SEVEN_RIDE_NUM'] + station['SEVEN_ALIGHT_NUM']
                n_8 = station['EIGHT_RIDE_NUM'] + station['EIGHT_ALIGHT_NUM']
                n_9 = station['NINE_RIDE_NUM'] + station['NINE_ALIGHT_NUM']
                n_10 = station['TEN_RIDE_NUM'] + station['TEN_ALIGHT_NUM']
                n_11 = station['ELEVEN_RIDE_NUM'] + station['ELEVEN_ALIGHT_NUM']
                n_12 = station['TWELVE_RIDE_NUM'] + station['TWELVE_ALIGHT_NUM']
                n_13 = station['THIRTEEN_RIDE_NUM'] + station['THIRTEEN_ALIGHT_NUM']
                n_14 = station['FOURTEEN_RIDE_NUM'] + station['FOURTEEN_ALIGHT_NUM']
                n_15 = station['FIFTEEN_RIDE_NUM'] + station['FIFTEEN_ALIGHT_NUM']
                n_16 = station['SIXTEEN_RIDE_NUM'] + station['SIXTEEN_ALIGHT_NUM']
                n_17 = station['SEVENTEEN_RIDE_NUM'] + station['SEVENTEEN_ALIGHT_NUM']
                n_18 = station['EIGHTEEN_RIDE_NUM'] + station['EIGHTEEN_ALIGHT_NUM']
                n_19 = station['NINETEEN_RIDE_NUM'] + station['NINETEEN_ALIGHT_NUM']
                n_20 = station['TWENTY_RIDE_NUM'] + station['TWENTY_ALIGHT_NUM']
                n_21 = station['TWENTY_ONE_RIDE_NUM'] + station['TWENTY_ONE_ALIGHT_NUM']
                n_22 = station['TWENTY_TWO_RIDE_NUM'] + station['TWENTY_TWO_ALIGHT_NUM']
                n_23 = station['TWENTY_THREE_RIDE_NUM'] + station['TWENTY_THREE_ALIGHT_NUM']

                if busst_name not in check:
                    result.append(
                        {'busst_name': busst_name, 'n_24': n_24, 'n_1': n_1, 'n_2': n_2,'n_3': n_3, 'n_4': n_4, 'n_5': n_5, 'n_6': n_6, 'n_7': n_7,
                         'n_8': n_8, 'n_9': n_9,'n_10': n_10, 'n_11': n_11,'n_12': n_12, 'n_13': n_13, 'n_14': n_14, 'n_15': n_15, 'n_16': n_16,
                         'n_17': n_17, 'n_18': n_18,'n_19': n_19, 'n_20': n_20, 'n_21': n_21, 'n_22': n_22, 'n_23': n_23})
                    check.append(busst_name)

                ## 중복된 정류장
                else:
                    for res in result:
                        if res['busst_name'] == busst_name:
                            res['n_24'] += n_24
                            res['n_1'] += n_1
                            res['n_2'] += n_2
                            res['n_3'] += n_3
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

                            break

    # print(len(result))
    return result

def add_bus_pos(data_list):
    start = 1
    end = 1000

    stations = []

    while True:
        parameters = service_key + "/"
        parameters += "json" + "/"
        parameters += "busStopLocationXyInfo" + "/"
        parameters += str(start) + "/"
        parameters += str(end) + "/"

        url = service_url + parameters
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        decodeData = response.read().decode('utf-8')
        jsonData = json.loads(decodeData)

        #         print(jsonData)
        print(url)

        try:
            req_CODE = jsonData['busStopLocationXyInfo']['RESULT']['CODE']

            print(req_CODE)

            if req_CODE == 'INFO-000':
                stations_info = jsonData['busStopLocationXyInfo']['row']

                stations += stations_info

                print(stations_info)

                start += 1000
                end += 1000

            else:
                break

        except:
            break

    print(len(stations))

    for data in data_list:

        for station in stations:
            stop_name = station['STOP_NM']
            stop_name = re.sub("\(.*\)|\s-\s.*", "", stop_name)

            if data['busst_name'] == stop_name:
                data['XCODE'] = station['XCODE']
                data['YCODE'] = station['YCODE']

    return data_list

bus_st_list = get_bus_data()
bus_info = add_bus_pos(bus_st_list)
bus_result = []

for bus_data in bus_info:

    temp = []
    for elements in bus_data.values():
        temp.append(elements)
    bus_result.append(temp)

columns = ('정류장명', '24시~1시', '1시~2시', '2시~3시', '3시~4시', '4시~5시', '5시~6시', '6시~7시', '7시~8시', '8시~9시',
           '9시~10시', '10시~11시', '11시~12시', '12시~13시', '13시~14시', '14시~15시', '15시~16시', '16시~17시', '17시~18시',
           '18시~19시', '19시~20시', '20시~21시', '21시~22시', '22시~23시', '23시~24시', 'X좌표', 'Y좌표')

bus_table = pd.DataFrame(bus_result, columns=columns)
bus_table.to_csv("./bus_info.csv", encoding="cp949", mode='w', index=True)