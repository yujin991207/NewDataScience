import requests

access_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='

def get_request_url():
    url = 'http://apis.data.go.kr/1741000/TsunamiShelter3/getTsunamiShelter1List'
    params = {'serviceKey' : access_key, 'numOfRows': 10, 'pageNo' : 1}

    TsunamiShelter = requests.get(url, params = params)

    return TsunamiShelter.text

raw_xml = get_request_url()
print(raw_xml)