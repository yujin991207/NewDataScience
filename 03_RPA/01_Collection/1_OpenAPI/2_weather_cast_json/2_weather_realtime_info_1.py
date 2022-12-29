# 목적 : 파이썬 코드를 활용하여 OpenAPI 호출 자동화
# step1 : 각 openAPI를 제공하는 사이트에서 제공하는 샘플 프로그램을 확보한다.
import requests

access_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='

def get_request_url():
    url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst'
    params = {'serviceKey' : access_key,
              'numOfRows' : 10,
              'pageNo' : 1,
              'dataType' : 'JSON',
              'base_date' : '20221227',
              'base_time' : '1049',
              'nx' : 58,
              'ny' : 125
    }
    response = requests.get(url, params = params)

    return response.text

raw_json = get_request_url()
print(raw_json)