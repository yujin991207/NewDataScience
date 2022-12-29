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

raw_json = get_request_url(url,'DT_0001')
print(raw_json)