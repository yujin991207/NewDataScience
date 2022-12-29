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

obsList = ['DT_0001','DT_0004','DT_0013']

def get_request_url(url, obsCode):
    params = {'ServiceKey':access_key, 'ObsCode': obsCode, 'Date':date, 'ResultType':'json'}
    response = requests.get(url, params=params)
    return response.text


def json_to_df_info(raw_json):
    all_data = []
    column_list = ['record_time', 'air_temp']

    for record in raw_json['result']['data']:
        row_data = []
        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)

    return column_list, all_data


def weather_info_collector():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'

    for obsCode in obsList :

        raw_str_json = get_request_url(url, obsCode)

        if raw_str_json:
            raw_json = json.loads(raw_str_json)

        column_list, all_data = json_to_df_info(raw_json)

        #df = pandas.DataFrame(all_data, columns=column_list)

        #df_preprocessed = preprocess_df(df)

        #preprocessed_df_to_oracle(df_preprocessed)

raw_json = get_request_url(url, 'DT_0001')

column_list, all_data = json_to_df_info(raw_json)

df = pandas.DataFrame(all_data, columns=column_list)

print(df)