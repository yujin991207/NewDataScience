import pandas as pd
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

def json_to_df_info(raw_json):
    all_data = []
    column_list = ["performInst","bsnsNm","bsnsKind","tel","people",
                   "bsnsMainActvt","bsnsSdate","bsnsFdate","gugun","dataDay"]

    for record in raw_json['getTblAgedjobStusInfo']['body']['items']['item']:
        row_data = []
        for column_data in column_list:
            row_data.append(record.get(column_data))
        all_data.append(row_data)
    return column_list, all_data
# raw_json = get_request_url()
# print(raw_json)
raw_str_json = get_request_url()

if raw_str_json:
    raw_json = json.loads(raw_str_json)

column_list, all_data = json_to_df_info(raw_json)
#pass
#print(raw_str_json)
df = pd.DataFrame(all_data, columns = column_list)
#print(df)

file_name = f'노인일자리_사업_현황_서비스.csv'
df.to_csv(file_name, index = False)