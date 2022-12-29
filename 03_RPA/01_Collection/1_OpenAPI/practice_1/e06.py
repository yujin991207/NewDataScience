import requests
import pandas as pd
from xml.etree.ElementTree import parse
from xml.etree.ElementTree import fromstring

access_key = 'xMa0cbwrTEM1UQzMljSLPYi29E5u1BLZysXwaxEgC6n44Ymoi/V86yK/giMFMiKE8zuvzHcSYFHFKOwwUy8dtw=='
TOTAL_NUM = 650
MAX_TRANSACTION = 30

def xml_to_df(data_root,data_name):
    all_data = []
    column_list = []

    is_column_list = False
    for row in data_root.iter(data_name):
        row_data = []
        is_first = True

        for column in row.iter():
            if is_first:
                is_first = False
                continue
            row_data.append(column.text)

            if not is_column_list:
                column_list.append(column.tag)

        is_column_list = True
        all_data.append(row_data)

    return column_list, all_data

def get_request_url(page_no):
    url = 'http://apis.data.go.kr/1741000/TsunamiShelter3/getTsunamiShelter1List'
    params = {'serviceKey' : access_key, 'numOfRows': MAX_TRANSACTION, 'pageNo' : page_no}

    TsunamiShelter = requests.get(url, params = params)

    return TsunamiShelter.text

request_total_num = ( TOTAL_NUM // MAX_TRANSACTION ) + 1

rename_dict = {'id':'일련번호', 'sido_name':'시도명', 'sigungu_name':'시군구명', 'remarks':'대피지구명',
               'shel_nm':'대피장소명', 'address':'주소', 'lon':'경도', 'lat':'위도', 'shel_av':'수용가능인원수',
               'lenth':'해변으로부터거리', 'shel_div_type':'대피소 분류명', 'seismic':'내진적용여부', 'height':'해발높이'}

REDEFINE_COLUMNS = ['일련번호','시도명','시군구명','대피지구명','대피장소명','주소','수용가능인원수',
                    '대피소 분류명','해변으로부터거리','내진적용여부','해발높이','경도','위도']

all_data = pd.DataFrame(columns = REDEFINE_COLUMNS)

for page_no in range(1, request_total_num + 1):
    raw_xml = get_request_url(page_no)
    root = fromstring(raw_xml)

    #tree = parse("지진해일_긴급대피장소.xml")
    data_root = root
    #print(data_root)
    column_list, page_data = xml_to_df(data_root,'row')

    df = pd.DataFrame(page_data, columns=column_list)

    df.rename(columns=rename_dict, inplace=True)
    df = df[['일련번호','시도명','시군구명','대피지구명','대피장소명','주소','수용가능인원수','대피소 분류명','해변으로부터거리','내진적용여부','해발높이','경도','위도']]

    all_data = pd.concat([all_data, df], ignore_index=True)

print(all_data.shape)

all_data.to_csv('지진해일_긴급대피장소_통합.csv', index = False, encoding='cp949')

