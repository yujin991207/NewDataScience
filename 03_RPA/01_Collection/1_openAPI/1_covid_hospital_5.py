# 목적 : OpenAPI 수집 대용량 데이터에 대한 페이징 테스트
# step1

import requests
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring

access_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='
TOTAL_NUM = 102
MAX_TRANSACTION = 30

def get_request_url(page_no):
    url = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList'
    params = {'serviceKey' : access_key, 'numOfRows' : MAX_TRANSACTION, 'pageNo' : page_no}
    response = requests.get(url, params=params)

    return response.text

request_total_num = ( TOTAL_NUM // MAX_TRANSACTION ) + 1 # => 자투리값 (+1)

for page_no in range(1, request_total_num + 1):
    raw_xml = get_request_url(page_no)
    parse_xml = fromstring(raw_xml)

    ElementTree(parse_xml).write(f'코로나19관련_병원정보_응답_page{page_no}.xml', encoding = 'utf-8')