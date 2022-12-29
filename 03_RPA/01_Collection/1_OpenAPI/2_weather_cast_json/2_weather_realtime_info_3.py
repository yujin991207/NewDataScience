# 목적 : json 파싱
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

#yyyymmdd = '20221227'
day_time = '1102'
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

print(raw_str_json)