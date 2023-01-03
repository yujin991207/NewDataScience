# URL
# http://openapi.seoul.go.kr:8088/595944524879756a3735434365634d/json/bikeList/1/10

# 2회 나누어 호출하시기 바랍니다. 예) 1/1,000, 1001/2,000 (대여소 수 : '18.11월말기준 1,471개소)
# - 요청인자 : 요청타입(JSON만가능), 서비스명, 시작위치, 종료위치
# - 출력값 : 거치대개수, 대여소이름, 자전거주차총건수, 거치율, 위도, 경도, 대여소ID
import threading
import time
import requests
import json
import pandas as pd
import cx_Oracle
from datetime import datetime

now = datetime.now()
print(now)

def get_request_url():
    getURL = 'http://openapi.seoul.go.kr:8088/595944524879756a3735434365634d/json/bikeList/1/10'
    rentBikeStatus = requests.get(getURL)

    return rentBikeStatus.text

def get_parse_json(raw_json):
    all_data = []

    # 행
    for record in raw_json['rentBikeStatus']['row']:
        all_data.append(
            {"rackTotCnt": record.get("rackTotCnt") ,
             "stationName": record.get("stationName") ,
             "parkingBikeTotCnt": record.get("parkingBikeTotCnt") ,
             "shared": record.get("shared") ,
             "stationLatitude": record.get("stationLatitude") ,
             "stationLongitude": record.get("stationLongitude") ,
             "stationId": record.get("stationId"),
             }
        )
    return all_data

def json_to_df_info(raw_json):
    all_data = []
    column_list = ["rackTotCnt", "stationName", "parkingBikeTotCnt", "shared", "stationLatitude", "stationLongitude","stationId"]

    for record in raw_json['rentBikeStatus']['row']:
        all_data.append(
                [
                 record.get("rackTotCnt"), # 거치대개수
                 record.get("stationName"), # 대여소이름
                 record.get("parkingBikeTotCnt"), # 자전거주차총건수
                 record.get("shared"), # 거치율(대여 가능 자전거 수 / 거치대 수)
                 record.get("stationLatitude"), # 위도
                 record.get("stationLongitude"), # 경도
                 record.get("stationId"), # 대여소id
                ],
        )
    return column_list, all_data

def preprocessed_df_to_oracle(df):
    con = cx_Oracle.connect('open_source/1111@localhost:1521/xe')
    cur = con.cursor()

    # '대여소이름', '거치대개수', '남은자전거수', '거치율', '위도', '경도', '대여소ID'
    sql_insert = '''
            insert into bike_real_time values(:대여소이름,:거치대개수,:남은자전거수,:거치율,:위도,:경도,:대여소ID,:제공시각)
            '''
    for i in range(len(df)):
        대여소이름 = df.iloc[i]['대여소이름']
        거치대개수 = df.iloc[i]['거치대개수']
        남은자전거수 = df.iloc[i]['남은자전거수']
        거치율 = df.iloc[i]['거치율']
        위도 = df.iloc[i]['위도']
        경도 = df.iloc[i]['경도']
        대여소ID = df.iloc[i]['대여소ID']
        제공시각 = df.iloc[i]['제공시각']

        cur.execute(sql_insert,
                    (대여소이름, 거치대개수, 남은자전거수, 거치율, 위도, 경도, 대여소ID, 제공시각)
                    )

    con.commit()
    cur.close()
    con.close()

def bike_real_time_info_collector():
    raw_str_json = get_request_url()

    if raw_str_json:
        raw_json = json.loads(raw_str_json)

        #parsed_json = get_parse_json(raw_json)

    column_list, all_data = json_to_df_info(raw_json)

    df = pd.DataFrame(all_data, columns = column_list)

    df = df[['stationName', 'rackTotCnt', 'parkingBikeTotCnt', 'shared', 'stationLatitude', 'stationLongitude',
                     'stationId']]
    df.columns = ['대여소이름', '거치대개수', '남은자전거수', '거치율', '위도', '경도', '대여소ID']
    df['제공시각'] = df['제공시각'] = datetime.now()

    preprocessed_df_to_oracle(df)

    file_name = '실시간_따릉이_대여정보.csv'
    df.to_csv(file_name, index=False, encoding='cp949')

    #print(raw_str_json)

# file_name = '실시간_따릉이_대여정보.json'
#
# with open(file_name, 'w', encoding ='utf8') as outfile:
#     retJson = json.dumps(parsed_json, indent = 4, sort_keys = True, ensure_ascii = False)
#
#     outfile.write(retJson)
#
# print(f'{file_name} SAVED\n')

#print(df)
#bike_real_time_info_collector()
def bike_real_time_info_scheduler():
    print('실시간 따릉이 정보 스케줄러 동작.\n')
    while True:
        bike_real_time_info_collector()
        print("수집완료.")
        time.sleep(60)

def print_main_menu():
    print('\n1. 따릉이 실시간 데이터 구축')
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
        t = threading.Thread(target=bike_real_time_info_scheduler(), daemon=True)
        t.start()
    elif(menu_num == 2):
        break
    elif (menu_num == 0):
        continue
