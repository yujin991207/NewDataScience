import requests
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring

access_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='

def get_request_url():
    url = 'http://apis.data.go.kr/1741000/TsunamiShelter3/getTsunamiShelter1List'
    params = {'serviceKey' : access_key, 'numOfRows': 10, 'pageNo' : 1}

    TsunamiShelter = requests.get(url, params = params)

    if TsunamiShelter.status_code == 200:
        return TsunamiShelter.text

    else:
        print(f'비정상 응답 : {TsunamiShelter.status_code}')
        return None

raw_xml = get_request_url()
parse_xml = fromstring(raw_xml)

ElementTree(parse_xml).write('지진해일_긴급대피장소.xml', encoding = 'utf-8')