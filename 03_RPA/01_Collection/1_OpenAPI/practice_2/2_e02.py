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

def get_parse_json(raw_json):
    all_data = []

    for record in raw_json['getTblAgedjobStusInfo']['body']['items']['item']:
        all_data.append(
            {"performInst" : record.get("performInst"),
             "bsnsNm" : record.get("bsnsNm"),
             "bsnsKind" : record.get("bsnsKind"),
             "tel" : record.get("tel"),
             "people" : record.get("people"),
             "bsnsMainActvt" : record.get("bsnsMainActvt"),
             "bsnsSdate" : record.get("bsnsSdate"),
             "bsnsFdate" : record.get("bsnsFdate"),
             "gugun" : record.get("gugun"),
             "dataDay" : record.get("dataDay")}
        )
    return all_data
# raw_json = get_request_url()
# print(raw_json)
raw_str_json = get_request_url()

if raw_str_json:
    raw_json = json.loads(raw_str_json)

parsed_json = get_parse_json(raw_json)
#pass
#print(raw_str_json)
file_name = f'노인일자리_사업_현황_서비스.json'

with open(file_name, 'w', encoding ='utf8') as outfile:
    retJson = json.dumps(parsed_json, indent = 4, sort_keys = True, ensure_ascii = False)

    outfile.write(retJson)

print(f'{file_name} SAVED\n')