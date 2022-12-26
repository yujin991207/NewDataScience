# 목적 : XML 데이터를 데이터프레임으로 변환테스트

import requests
import pandas as pd
from xml.etree.ElementTree import parse

def xml_to_df(data_root,data_name):
    all_data = []
    column_list = []

    is_column_list = False # => tag만 가지고 text를 추출 할 수 있기 때문에 False로 준다.
    for row in data_root.iter(data_name):
        row_data = []
        is_first = True

        for column in row.iter(): # => items의 자식노드 이름이 각각 다르기 때문에 이름을 지정할 수 없다.
            if is_first:
                is_first = False
                continue
            row_data.append(column.text) # => 열의 text값

            if not is_column_list:
                column_list.append(column.tag) # => 열이름

        is_column_list = True
        all_data.append(row_data)

    return column_list, all_data

tree = parse("코로나19관련_병원정보_응답.xml")
data_root = tree.getroot().find('body').find('items')

column_list, all_data = xml_to_df(data_root,'item')

df = pd.DataFrame(all_data, columns = column_list)
df.to_csv('코로나19관련_병원정보_응답.csv', index = False)
print(df)


