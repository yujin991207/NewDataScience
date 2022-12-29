# 목적 : 업데이트 주기에 맞추어 시간 파라미터 설정
# OpenAPI에서 최신 데이터를 가져오는 테크닉.
import requests
import datetime
import time
import json

access_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='

def get_request_url():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'serviceKey' : access_key,
              'numOfRows' : 10,
              'pageNo' : 1,
              'dataType' : 'JSON',
              'base_date' : base_date,
              'base_time' : day_time,
              'nx' : x_coodinate,
              'ny' : y_coodinate
    }
    response = requests.get(url, params = params)

    return response.text

def get_parse_json(raw_json):
    all_data = []

    # 행
    for record in raw_json['response']['body']['items']['item']:
        all_data.append(
            {"baseDate": record.get("baseDate"),
            #"baseDate" : record['baseDate']
             "baseTime": record.get("baseTime"),
             "category": record.get("category"),
             "nx": record.get("nx"),
             "ny": record.get("ny"),
             "obsrValue": record.get("obsrValue")}
        )
    return all_data

def get_update_time_info():
    day_hour = time.strftime('%H')
    day_min = time.strftime('%M')

    day_min_int = int(day_min)

    if (day_min_int >= 40) and (day_min_int < 60):
        # 실시간 업데이트 구간
        day_time = time.strftime('%H%M') # <= 현재 시간분
    else:
        # 최신데이터 업데이트 구간
        # 보통 업데이트는 30분을 기준으로 함. (메뉴얼에는 40분으로 명시)
        day_hour_int = int(day_hour)
        # 0~23시
        # 0시에서 -1을 하면 ... 23시이기때문에
        if day_hour_int == 0:
            day_hour_int = 23
        else:
            day_hour_int = day_hour_int - 1

            # 시간은 60분 단위이므로 30분 미만은 30분을 빼고 보수의 개념으로 60을 더한다.
            # ex) 12:30 에서 40분을 빼면 ... 11:50 이기때문에
            #     (30 - 40) + 60 = 50
            revised_min = 60 + (day_min_int - 40)
            day_time = "{0:0>2}".format(day_hour_int) + str(revised_min)

    return day_time

#yyyymmdd = '20221227'
#day_time = '1102'
day_time = get_update_time_info()
base_date = time.strftime('%Y%m%d')
#day_time = time.strftime('%H%M')
# 00분~40분 구간은 최신 정보가 없음. / 41분~59분 구간은 최신 정보가 있음.
# 구로구 구로동 좌표
x_coodinate = '58'
y_coodinate = '125'

raw_str_json = get_request_url() # <= str타입이기때문에 dict타입으로 변경해줘야한다.

if raw_str_json:
    raw_json = json.loads(raw_str_json)
    # json.loads() 문자열 json을 실제 json(dict)타입으로 변환

parsed_json = get_parse_json(raw_json)

#print(raw_str_json)

file_name = f'초단기날씨현황_조회_{base_date}_{day_time}.json'

with open(file_name, 'w', encoding ='utf8') as outfile:
    retJson = json.dumps(parsed_json, indent = 4, sort_keys = True, ensure_ascii = False)

    outfile.write(retJson)

print(f'{file_name} SAVED\n')