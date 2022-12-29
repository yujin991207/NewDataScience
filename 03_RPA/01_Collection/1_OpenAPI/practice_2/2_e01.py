import requests
import json

acces_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='

def get_request_url():
    url = 'http://apis.data.go.kr/6260000/BusanTblAgedjobStusService/getTblAgedjobStusInfo'
    params ={
        'serviceKey' : acces_key,
        'numOfRows' : 30,
        'pageNo' : 1,
        'resultType' : 'JSON'
    }
    getTblAgedjobStusInfo = requests.get(url, params = params)

    return getTblAgedjobStusInfo.text

raw_json = get_request_url()
print(raw_json)
