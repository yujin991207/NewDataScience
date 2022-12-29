# 목적 : 열데이터 추가 자동화
import pandas as pd
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

def json_to_df_info(raw_json):
    all_data = []
    column_list = ["baseDate", "baseTime", "category", "nx", "ny", "obsrValue"]

    for record in raw_json['response']['body']['items']['item']:
        row_data = []
        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)
    return column_list, all_data

#yyyymmdd = '20221227'
#day_time = '1102'
base_date = time.strftime('%Y%m%d')
day_time = get_update_time_info()
#day_time = time.strftime('%H%M')
# 00분~40분 구간은 최신 정보가 없음. / 41분~59분 구간은 최신 정보가 있음.
# 구로구 구로동 좌표
x_coodinate = '58'
y_coodinate = '125'

raw_str_json = get_request_url() # <= str타입이기때문에 dict타입으로 변경해줘야한다.

if raw_str_json:
    raw_json = json.loads(raw_str_json)
    # json.loads() 문자열 json을 실제 json(dict)타입으로 변환

column_list, all_data = json_to_df_info(raw_json)

df = pd.DataFrame(all_data, columns = column_list)
#print(df)
#pass
#print(raw_str_json)

file_name = f'초단기날씨현황_조회_{base_date}_{day_time}.csv'
df.to_csv(file_name, index = False)
#
# with open(file_name, 'w', encoding ='utf8') as outfile:
#     retJson = json.dumps(parsed_json, indent = 4, sort_keys = True, ensure_ascii = False)
#
#     outfile.write(retJson)
#
# print(f'{file_name} SAVED\n')

# baseDate : 발표일자
# baseTime : 발표시각
# nx : 예보지점 x 좌표
# ny : 예보지점 y 좌표

# category : 자료구분코드
    # T1H	기온		℃
    # RN1	1시간 강수량	mm
    # UUU	동서바람성분	m/s
    # VVV	남북바람성분	m/s
    # REH	습도		%
    # PTY	강수형태		코드값
    # VEC	풍향		deg
    # WSD	풍속		m/s

# obsrValue : 실황값 (실제값)