import pandas as pd
import re
subway_data = pd.read_csv('./subway_info_sigudong.csv', encoding= 'CP949', index_col= 0, header= 0, engine= 'python')
bus_data = pd.read_csv('./bus_info_sigudong.csv', encoding= 'CP949', index_col= 0, header= 0, engine= 'python')


areas = []

## 추가 함수
def add_data(csv_data, results):
    for idx,data in enumerate(subway_data['시구동']):
        if pd.isna(data) == False and data !=  '':
            str_data = re.sub('\d+동', '동', data)

            n_24 = csv_data['24시~1시'][idx]
            n_1 = csv_data['1시~2시'][idx]
            n_2 = csv_data['2시~3시'][idx]
            n_3 = csv_data['3시~4시'][idx]
            n_4 = csv_data['4시~5시'][idx]
            n_5 = csv_data['5시~6시'][idx]
            n_6 = csv_data['6시~7시'][idx]
            n_7 = csv_data['7시~8시'][idx]
            n_8 = csv_data['8시~9시'][idx]
            n_9 = csv_data['9시~10시'][idx]
            n_10 = csv_data['10시~11시'][idx]
            n_11 = csv_data['11시~12시'][idx]
            n_12 = csv_data['12시~13시'][idx]
            n_13 = csv_data['13시~14시'][idx]
            n_14 = csv_data['14시~15시'][idx]
            n_15 = csv_data['15시~16시'][idx]
            n_16 = csv_data['16시~17시'][idx]
            n_17 = csv_data['17시~18시'][idx]
            n_18 = csv_data['18시~19시'][idx]
            n_19 = csv_data['19시~20시'][idx]
            n_20 = csv_data['20시~21시'][idx]
            n_21 = csv_data['21시~22시'][idx]
            n_22 = csv_data['22시~23시'][idx]
            n_23 = csv_data['23시~24시'][idx]

            total = n_1 + n_2 + n_3 + n_4 + n_5 + n_6 + n_7 + n_8 + n_9 + n_10 + n_11 + n_12 + n_13 \
                    + n_14 + n_15 + n_16 + n_17 + n_18 + n_19 + n_20 + n_21 + n_22 + n_23 + n_24

            if str_data not in areas:
                areas.append(str_data)
                results.append(
                    {'area_name': str_data, 'n_24': n_24, 'n_1': n_1, 'n_2': n_2,'n_3': n_3, 'n_4': n_4, 'n_5': n_5, 'n_6': n_6, 'n_7': n_7,
                             'n_8': n_8, 'n_9': n_9,'n_10': n_10, 'n_11': n_11,'n_12': n_12, 'n_13': n_13, 'n_14': n_14, 'n_15': n_15, 'n_16': n_16,
                             'n_17': n_17, 'n_18': n_18,'n_19': n_19, 'n_20': n_20, 'n_21': n_21, 'n_22': n_22, 'n_23': n_23, 'total': total})

            ## 중복지역
            else:
                for result in results:
                    if result['area_name'] == str_data:
                        result['n_24'] += n_24
                        result['n_1'] += n_1
                        result['n_2'] += n_2
                        result['n_3'] += n_3
                        result['n_4'] += n_4
                        result['n_5'] += n_5
                        result['n_6'] += n_6
                        result['n_7'] += n_7
                        result['n_8'] += n_8
                        result['n_9'] += n_9
                        result['n_10'] += n_10
                        result['n_11'] += n_11
                        result['n_12'] += n_12
                        result['n_13'] += n_13
                        result['n_14'] += n_14
                        result['n_15'] += n_15
                        result['n_16'] += n_16
                        result['n_17'] += n_17
                        result['n_18'] += n_18
                        result['n_19'] += n_19
                        result['n_20'] += n_20
                        result['n_21'] += n_21
                        result['n_22'] += n_22
                        result['n_23'] += n_23
                        result['total'] += total

                        break

    return results


results = []

## 지하철 버스 데이터 추가
results = add_data(subway_data, results)
results = add_data(bus_data, results)
areas.sort()
print(areas)

float_population_result = []

for result in results:

    temp = []
    for elements in result.values():
        temp.append(elements)
    float_population_result.append(temp)

columns = ('지역', '24시~1시', '1시~2시', '2시~3시', '3시~4시', '4시~5시', '5시~6시', '6시~7시', '7시~8시', '8시~9시',
           '9시~10시', '10시~11시', '11시~12시', '12시~13시', '13시~14시', '14시~15시', '15시~16시', '16시~17시', '17시~18시',
           '18시~19시', '19시~20시', '20시~21시', '21시~22시', '22시~23시', '23시~24시', '총합')

result_table = pd.DataFrame(float_population_result, columns= columns)
result_table = result_table.sort_values(by=['지역'], ascending=True)
result_table.to_csv("./float_population_result.csv", encoding="cp949", mode='w', index = True)