import requests
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring

access_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='
TOTAL_NUM = 650
MAX_TRANSACTION = 30
def get_request_url(page_no):
    url = 'http://apis.data.go.kr/1741000/TsunamiShelter3/getTsunamiShelter1List'
    params = {'serviceKey' : access_key, 'numOfRows': 10, 'pageNo' : 1}

    TsunamiShelter = requests.get(url, params = params)

    return TsunamiShelter.text

request_total_num = ( TOTAL_NUM // MAX_TRANSACTION ) + 1

for page_no in range(1, request_total_num + 1):
    raw_xml = get_request_url(page_no)
    parse_xml = fromstring(raw_xml)

    #ElementTree(parse_xml).write(f'지진해일_긴급대피장소_page{page_no}.xml', encoding = 'utf-8')