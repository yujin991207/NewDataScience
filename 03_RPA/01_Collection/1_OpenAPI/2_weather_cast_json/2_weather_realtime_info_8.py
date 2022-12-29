# 목적 : 분석을 위한 데이터 전처리
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

# * 데이터병합 => 데이터포맷을 변경 할 필요가 있어보임... (전처리)
#
# (전)
# baseDate	baseTime	category	nx	    ny	    obsrValue
# 20221227	1200	      PTY	    58	    125	        0
# 20221227	1200	      REH	    58	    125	        41
#
# =============================================================================================
#
# (후)
# baseDate + baseTime	    nx	    ny	    PTY	    REH	    RN1	    T1H	    UUU	    VEC	    VVV	    WSD
#    202212271200	        58	    125	     0	     41	     0	    2.7	    0.3	    201	    0.8	    0.9
def preprocess_df(df):
    df.insert(0,'date_time', df['baseDate'] + df['baseTime'])

    p_df = pd.pivot_table(df, index = 'date_time', columns = 'category', values = 'obsrValue')
    nx = df.loc[0,'nx']
    ny = df.loc[0, 'ny']

    p_df.insert(0,'nx',[nx])
    p_df.insert(1, 'ny', [ny])
    #pass
    return p_df
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

df_preprocessed = preprocess_df(df)

file_name = f'초단기날씨현황_조회_{base_date}_{day_time}.csv'
df_preprocessed.to_csv(file_name)