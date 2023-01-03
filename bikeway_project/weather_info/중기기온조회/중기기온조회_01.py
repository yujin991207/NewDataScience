# 중기기온조회 : 예보구역코드, 발표시각의 조회 조건으로 예보일로부터 3일에서 10일까지 최저/최고기온정보를  조회하는 기능
#
#  중기기온예보구역 => 수도권만
# 11B10101	서울
# 11B20201	인천
# 11B20601	수원

# URL
# http://apis.data.go.kr/1360000/MidFcstInfoService/getMidTa?serviceKey=xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw==&numOfRows=10&pageNo=1&dataType=JSON&regId=11B10101&tmFc=202301030600

import threading
import time
import requests
import json
import pandas as pd
import cx_Oracle
from datetime import datetime

access_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='

# 불러올 지역 코드 => 서울, 인천, 수원
regId_dict = {'11B10101':'서울','11B20201':'인천','11B20601':'수원'}

def get_request_url(regId):
    url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidTa'
    params = {'serviceKey' : access_key,
              'numOfRows' : 10,
              'pageNo' : 1,
              'dataType' : 'JSON',
              'regId' : regId,
              'tmFc' : '202301030600'
    }
    response = requests.get(url, params = params)

    return response.text

def get_parse_json(raw_json):
    all_data = []

    # 행
    for record in raw_json['response']['body']['items']['item']:
        all_data.append(
            {
                "regId": record.get("regId"),

                 "taMin3": record.get("taMin3"),
                 "taMin3Low": record.get("taMin3Low"),
                 "taMin3High": record.get("taMin3High"),
                 "taMax3": record.get("taMax3"),
                 "taMax3Low": record.get("taMax3Low"),
                 "taMax3High": record.get("taMax3High"),

                "taMin4": record.get("taMin4"),
                "taMin4Low": record.get("taMin4Low"),
                "taMin4High": record.get("taMin4High"),
                "taMax4": record.get("taMax4"),
                "taMax4Low": record.get("taMax4Low"),
                "taMax4High": record.get("taMax4High"),

                "taMin5": record.get("taMin5"),
                "taMin5Low": record.get("taMin5Low"),
                "taMin5High": record.get("taMin5High"),
                "taMax5": record.get("taMax5"),
                "taMax5Low": record.get("taMax5Low"),
                "taMax5High": record.get("taMax5High"),

                "taMin6": record.get("taMin6"),
                "taMin6Low": record.get("taMin6Low"),
                "taMin6High": record.get("taMin6High"),
                "taMax6": record.get("taMax6"),
                "taMax6Low": record.get("taMax6Low"),
                "taMax6High": record.get("taMax6High"),

                "taMin7": record.get("taMin7"),
                "taMin7Low": record.get("taMin7Low"),
                "taMin7High": record.get("taMin7High"),
                "taMax7": record.get("taMax7"),
                "taMax7Low": record.get("taMax7Low"),
                "taMax7High": record.get("taMax7High"),

                "taMin8": record.get("taMin8"),
                "taMin8Low": record.get("taMin8Low"),
                "taMin8High": record.get("taMin8High"),
                "taMax8": record.get("taMax8"),
                "taMax8Low": record.get("taMax8Low"),
                "taMax8High": record.get("taMax8High"),

                "taMin9": record.get("taMin9"),
                "taMin9Low": record.get("taMin9Low"),
                "taMin9High": record.get("taMin9High"),
                "taMax9": record.get("taMax9"),
                "taMax9Low": record.get("taMax9Low"),
                "taMax9High": record.get("taMax9High"),

                "taMin10": record.get("taMin10"),
                "taMin10Low": record.get("taMin10Low"),
                "taMin10High": record.get("taMin10High"),
                "taMax10": record.get("taMax10"),
                "taMax10Low": record.get("taMax10Low"),
                "taMax10High": record.get("taMax10High")

            }
        )
    return all_data

def json_to_df_info(raw_json):
    all_data = []
    column_list = [
                    "regId",
                    "taMin3",
                    "taMax3",
                    "taMax3Low",
                    "taMax3High",
                    "taMin4",
                    "taMin4Low",
                    "taMin4High",
                    "taMax4",
                    "taMax4Low",
                    "taMax4High",
                    "taMin5",
                    "taMin5Low",
                    "taMin5High",
                    "taMax5",
                    "taMax5Low",
                    "taMax5High",
                    "taMin6",
                    "taMin6Low",
                    "taMin6High",
                    "taMax6",
                    "taMax6Low",
                    "taMax6High",
                    "taMin7",
                    "taMin7Low",
                    "taMin7High",
                    "taMax7",
                    "taMax7Low",
                    "taMax7High",
                    "taMin8",
                    "taMin8Low",
                    "taMin8High",
                    "taMax8",
                    "taMax8Low",
                    "taMax8High",
                    "taMin9",
                    "taMin9Low",
                    "taMin9High",
                    "taMax9",
                    "taMax9Low",
                    "taMax9High",
                    "taMin10",
                    "taMin10Low",
                    "taMin10High",
                    "taMax10",
                    "taMax10Low",
                    "taMax10High"
                    ]

    for record in raw_json['response']['body']['items']['item']:
        all_data.append(
                [
                    record.get("regId"),

                    record.get("taMin3"),
                    record.get("taMin3Low"),
                    record.get("taMin3High"),
                    record.get("taMax3"),
                    record.get("taMax3Low"),
                    record.get("taMax3High"),

                    record.get("taMin4"),
                    record.get("taMin4Low"),
                    record.get("taMin4High"),
                    record.get("taMax4"),
                    record.get("taMax4Low"),
                    record.get("taMax4High"),

                    record.get("taMin5"),
                    record.get("taMin5Low"),
                    record.get("taMin5High"),
                    record.get("taMax5"),
                    record.get("taMax5Low"),
                    record.get("taMax5High"),

                    record.get("taMin6"),
                    record.get("taMin6Low"),
                    record.get("taMin6High"),
                    record.get("taMax6"),
                    record.get("taMax6Low"),
                    record.get("taMax6High"),

                    record.get("taMin7"),
                    record.get("taMin7Low"),
                    record.get("taMin7High"),
                    record.get("taMax7"),
                    record.get("taMax7Low"),
                    record.get("taMax7High"),

                    record.get("taMin8"),
                    record.get("taMin8Low"),
                    record.get("taMin8High"),
                    record.get("taMax8"),
                    record.get("taMax8Low"),
                    record.get("taMax8High"),

                    record.get("taMin9"),
                    record.get("taMin9Low"),
                    record.get("taMin9High"),
                    record.get("taMax9"),
                    record.get("taMax9Low"),
                    record.get("taMax9High"),

                    record.get("taMin10"),
                    record.get("taMin10Low"),
                    record.get("taMin10High"),
                    record.get("taMax10"),
                    record.get("taMax10Low"),
                    record.get("taMax10High")
                ]
        )
    return column_list, all_data

def weather_temp_info_collector() :
    # today = datetime.today().strftime('$Y$m$d')

    for regId in regId_dict:
        raw_str_json = get_request_url(regId)

        if raw_str_json:
            raw_json = json.loads(raw_str_json)
            # json.loads() 문자열 json을 실제 json(dict)타입으로 변환

        parsed_json = get_parse_json(raw_json)

        #print(raw_str_json)

        #print(raw_json)
        column_list, all_data = json_to_df_info(raw_json)

        df = pd.DataFrame(all_data, columns = column_list)
        print(df)

# file_name = '중기기온조회_수도권.csv'
# df.to_csv(file_name, index = False)

#file_name = '중기기온조회_수도권.json'
#
# with open(file_name, 'w', encoding ='utf8') as outfile:
#     retJson = json.dumps(parsed_json, indent = 4, sort_keys = True, ensure_ascii = False)
#
#     outfile.write(retJson)
#
# print(f'{file_name} SAVED\n')
weather_temp = weather_temp_info_collector()

print(weather_temp)