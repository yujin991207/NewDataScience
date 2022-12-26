# 목적 : XML 응답을 XML로 저장하기
# 이유 : OpenAPI 호출 할 때마다 일일 호출 건수가 차감되기때문에
#         => XML의 구조를 파악해야하므로 XML로 저장해본다.

import requests
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import fromstring
# fromstring : 텍스트 xml을 실제 xml 타입으로 변환

access_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='

def get_request_url():
    url = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList'
    params = {'serviceKey' : access_key, 'numOfRows' : 10, 'pageNo' : 1}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.text
    else:
        print(f'비정상 응답 : status_code => {response.status_code}')
        return None


raw_xml = get_request_url()
parse_xml = fromstring(raw_xml)

ElementTree(parse_xml).write('코로나19관련_병원정보_응답.xml', encoding='utf-8')