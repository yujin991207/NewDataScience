import threading
import time
import requests
import json
import pandas
import cx_Oracle

# http://www.khoa.go.kr/api/oceangrid/tideObsAirTemp/search.do?ServiceKey=hRfuERzasg3WVKibaLkKQ==&ObsCode=DT_0016&Date=20221227&ResultType=json

# obs_post_id	관측소 ID
# obs_post_name	관측소 명
# obs_lat	관측소 위도
# obs_lon	관측소 경도
# record_time	관측시간
# air_temp	기온
# obs_last_req_cnt	금일요청가능횟수
from requests import get

access_key = 'hRfuERzasg3WVKibaLkKQ=='
url = 'http://www.khoa.go.kr/api/oceangrid/tideObsAirTemp/search.do'
date = 20221228

obsDict = {'DT_0001':'인천','DT_0004':'제주','DT_0013':'울릉도'}

def get_request_url(url, obsCode):
    params = {'ServiceKey':access_key, 'ObsCode': obsCode, 'Date':date, 'ResultType':'json'}
    response = requests.get(url, params=params)
    return response.text

def json_to_df_info(obsCode, raw_json):
    all_data = []
    column_list = ['record_time', 'air_temp']

    for record in raw_json['result']['data']:
        row_data = []
        row_data.append(obsCode);
        row_data.append(obsDict[obsCode]);
        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)

    #column_list = ['obs_post_id', 'obs_post_name', 'record_time', 'air_temp']
    column_list = ['관측소코드', '관측소명', '관측시간', '기온']
    return column_list, all_data

def preprocessed_df_to_oracle(df):
    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()
    sql_insert = '''
            insert into air_temp values(:관측소코드,:관측소명,:관측시간,:기온)
            '''
    관측소코드 = df.iloc[len(df)-1]['관측소코드']
    관측소명 = df.iloc[len(df)-1]['관측소명']  # int 값에 대해서는 int 형으로 변환해줘야 한다.
    관측시간 = df.iloc[len(df)-1]['관측시간']
    기온 = df.iloc[len(df)-1]['기온']

    cur.execute(sql_insert,
                (관측소코드,관측소명,관측시간,기온)
                )
    con.commit()
    cur.close()
    con.close()

def air_temp_info_collector() :
    for obsCode in obsDict :

        raw_str_json = get_request_url(url, obsCode) # <= str타입이기때문에 dict타입으로 변경해줘야한다.

        if raw_str_json:
            raw_json = json.loads(raw_str_json)
            # json.loads() 문자열 json을 실제 json(dict)타입으로 변환

        column_list, all_data = json_to_df_info(obsCode, raw_json)

        df = pandas.DataFrame(all_data, columns = column_list)
        #print(df)
        preprocessed_df_to_oracle(df)


def air_temp_info_scheduler():
    print('기온정보 수집기 스케줄러 동작.\n')
    while True:
        air_temp_info_collector()
        print("수집완료.")
        time.sleep(60) # 1분 주기로 데이터 수집

def print_main_menu():
    print('\n1. 기온데이터 실시간 데이터 구축')
    print('2. 스케줄러 종료')
    print('* 엔터: 메뉴 업데이트\n')

while True:
    print_main_menu()
    print('아래행에 메뉴입력: ')
    selection = input()
    if selection == '': continue
    else:                menu_num = int(selection)

    if(menu_num == 1):
        t = threading.Thread(target=air_temp_info_scheduler, daemon=True)
        t.start()
    elif(menu_num == 2):
        break
    elif (menu_num == 0):
        continue