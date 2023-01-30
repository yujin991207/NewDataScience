# 중기육상예보구역 : 예보구역코드, 발표시각의 조회 조건으로 예보일로부터 3일에서 10일까지 육상날씨정보를 조회하는 기능
# 11B00000	서울, 인천, 경기도
#
# http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst?serviceKey=xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw==&numOfRows=10&pageNo=1&dataType=JSON&regId=11B00000&tmFc=202301030600

import threading
import time
import requests
import json
import datetime

import pandas as pd
import cx_Oracle

access_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='

regId_dict = {'11B00000' : '수도권'}

def get_request_url(regId,yyyymmdd):
    url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst'
    params = {'serviceKey' : access_key,
              'numOfRows' : 10,
              'pageNo' : 1,
              'dataType' : 'JSON',
              'regId' : regId,
              'tmFc' : yyyymmdd
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

                 "rnSt3Am": record.get("rnSt3Am"),
                 "rnSt3Pm": record.get("rnSt3Pm"),

                 "rnSt4Am": record.get("rnSt4Am"),
                 "rnSt4Pm": record.get("rnSt4Pm"),

                 "rnSt5Am": record.get("rnSt5Am"),
                 "rnSt5Pm": record.get("rnSt5Pm"),

                "rnSt6Am": record.get("rnSt6Am"),
                "rnSt6Pm": record.get("rnSt6Pm"),

                "rnSt7Am": record.get("rnSt7Am"),
                "rnSt7Pm": record.get("rnSt7Pm"),

# ============================================================

                "wf3Am": record.get("wf3Am"),
                "wf3Pm": record.get("wf3Pm"),

                "wf4Am": record.get("wf4Am"),
                "wf4Pm": record.get("wf4Pm"),

                "wf5Am": record.get("wf5Am"),
                "wf5Pm": record.get("wf5Pm"),

                "wf6Am": record.get("wf6Am"),
                "wf6Pm": record.get("wf6Pm"),

                "wf7Am": record.get("wf7Am"),
                "wf7Pm": record.get("wf7Pm")
            }
        )
    return all_data

def json_to_df_info(raw_json,regId):
    all_data = []
    column_list = ["rnSt3Am", "wf3Am", "rnSt3Pm", "wf3Pm", "rnSt4Am", "wf4Am", "rnSt4Pm",  "wf4Pm", "rnSt5Am", "wf5Am", "rnSt5Pm", "wf5Pm",
                   "rnSt6Am", "wf6Am", "rnSt6Pm", "wf6Pm", "rnSt7Am", "wf7Am", "rnSt7Pm", "wf7Pm"]

    for record in raw_json['response']['body']['items']['item']:
        row_data = []
        row_data.append(regId_dict[regId])
        # print(row_data)

        for column in column_list:
            row_data.append(record.get(column))
    all_data.append(row_data)

    column_list = ['AREANAME',
                   'RAIN_1_AM', 'WEATHER_1_AM', 'RAIN_1_PM', 'WEATHER_1_PM',
                   'RAIN_2_AM', 'WEATHER_2_AM', 'RAIN_2_PM', 'WEATHER_2_PM',
                    'RAIN_3_AM', 'WEATHER_3_AM', 'RAIN_3_PM', 'WEATHER_3_PM',
                   'RAIN_4_AM', 'WEATHER_4_AM', 'RAIN_4_PM', 'WEATHER_4_PM',
                    'RAIN_5_AM', 'WEATHER_5_AM', 'RAIN_5_PM', 'WEATHER_5_PM']

    return column_list, all_data


def preprocessed_df_to_oracle(df):
        con = cx_Oracle.connect('bike/12345@192.168.0.78:1521/xe')
        cur = con.cursor()
        sql_insert = '''
                insert into weather_rain( AREANAME,
                RAIN_1_AM, WEATHER_1_AM, RAIN_1_PM, WEATHER_1_PM,
                RAIN_2_AM, WEATHER_2_AM, RAIN_2_PM, WEATHER_2_PM,
                RAIN_3_AM, WEATHER_3_AM, RAIN_3_PM, WEATHER_3_PM,
                RAIN_4_AM, WEATHER_4_AM, RAIN_4_PM, WEATHER_4_PM,
                RAIN_5_AM, WEATHER_5_AM, RAIN_5_PM, WEATHER_5_PM,UPDATETIME) 
                
                values( :AREANAME,
                 :RAIN_1_AM, :WEATHER_1_AM, :RAIN_1_PM, :WEATHER_1_PM,
                 :RAIN_2_AM, :WEATHER_2_AM, :RAIN_2_PM, :WEATHER_2_PM,
                 :RAIN_3_AM, :WEATHER_3_AM, :RAIN_3_PM, :WEATHER_3_PM,
                 :RAIN_4_AM, :WEATHER_4_AM, :RAIN_4_PM, :WEATHER_4_PM,
                 :RAIN_5_AM, :WEATHER_5_AM, :RAIN_5_PM, :WEATHER_5_PM, :UPDATETIME)
                '''
        for i in range(len(df)):
            AREANAME = df.iloc[i]['AREANAME']

            RAIN_1_AM = int(df.iloc[i]['RAIN_1_AM'])
            WEATHER_1_AM = df.iloc[i]['WEATHER_1_AM']
            RAIN_1_PM = int(df.iloc[i]['RAIN_1_PM'])
            WEATHER_1_PM = df.iloc[i]['WEATHER_1_PM']

            RAIN_2_AM = int(df.iloc[i]['RAIN_2_AM'])
            WEATHER_2_AM = df.iloc[i]['WEATHER_2_AM']
            RAIN_2_PM = int(df.iloc[i]['RAIN_2_PM'])
            WEATHER_2_PM = df.iloc[i]['WEATHER_2_PM']

            RAIN_3_AM = int(df.iloc[i]['RAIN_3_AM'])
            WEATHER_3_AM = df.iloc[i]['WEATHER_3_AM']
            RAIN_3_PM = int(df.iloc[i]['RAIN_3_PM'])
            WEATHER_3_PM = df.iloc[i]['WEATHER_3_PM']

            RAIN_4_AM = int(df.iloc[i]['RAIN_4_AM'])
            WEATHER_4_AM = df.iloc[i]['WEATHER_4_AM']
            RAIN_4_PM = int(df.iloc[i]['RAIN_4_PM'])
            WEATHER_4_PM = df.iloc[i]['WEATHER_4_PM']

            RAIN_5_AM = int(df.iloc[i]['RAIN_5_AM'])
            WEATHER_5_AM = df.iloc[i]['WEATHER_5_AM']
            RAIN_5_PM = int(df.iloc[i]['RAIN_5_PM'])
            WEATHER_5_PM = df.iloc[i]['WEATHER_5_PM']

            UPDATETIME = df.iloc[i]['UPDATETIME']


            cur.execute(sql_insert,
                        ( AREANAME,
                         RAIN_1_AM, WEATHER_1_AM, RAIN_1_PM, WEATHER_1_PM,
                         RAIN_2_AM, WEATHER_2_AM, RAIN_2_PM, WEATHER_2_PM,
                         RAIN_3_AM, WEATHER_3_AM, RAIN_3_PM, WEATHER_3_PM,
                         RAIN_4_AM, WEATHER_4_AM, RAIN_4_PM, WEATHER_4_PM,
                         RAIN_5_AM, WEATHER_5_AM, RAIN_5_PM, WEATHER_5_PM,
                         UPDATETIME
                            )
                        )

        con.commit()
        cur.close()
        con.close()

def get_update_time_info():
    now = datetime.datetime.now()

    if now.hour < 18 and now.hour > 0:
        time = datetime.time(6,00,00)
        update_time = datetime.datetime.combine(now,time)

        print(f'시간 업데이트합니다.{update_time}')
    else:
        time = datetime.time(18,00,00)
        update_time = datetime.datetime.combine(now, time)

        print(f'시간 업데이트합니다.{update_time}')

    return update_time

def weather_rain_info_collector():

    #url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidLandFcst'
    update_time = get_update_time_info()
    yyyymmdd = update_time.strftime("%Y%m%d%H%M")

    #print(yyyymmdd)

    for regId in regId_dict:
        raw_str_json = get_request_url(regId,yyyymmdd)

        if raw_str_json:
                raw_json = json.loads(raw_str_json)

        column_list, all_data = json_to_df_info(raw_json,regId)

        df = pd.DataFrame(all_data, columns = column_list)
        df['UPDATETIME'] = df['UPDATETIME'] = datetime.datetime.now()
        print(df)
        preprocessed_df_to_oracle(df)


def weather_rain_info_scheduler():
    print('주간강수기온정보 수집기 스케줄러 동작.\n')
    while True:
        weather_rain_info_collector()
        print(f"수집완료")
        time.sleep(86500)

def print_main_menu():
    print('\n1. 주간날씨 강수데이터 실시간 데이터 구축')
    print('2. 스케줄러 종료')
    print('* 엔터: 메뉴 업데이트\n')

while True:
    print_main_menu()
    print('아래행에 메뉴입력: ')
    selection = input()
    if selection == '':
        continue
    else:
        menu_num = int(selection)

    if(menu_num == 1):
        date = get_update_time_info()
        t = threading.Thread(target=weather_rain_info_scheduler(), daemon=True)
        t.start()
    elif(menu_num == 2):
        break
    elif (menu_num == 0):
        continue

