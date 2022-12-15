# -*- coding: utf-8 -*-
from xml.etree.ElementTree import parse
import pandas as pd

tree = parse("12월14일_코로나_예방접종현황.xml")
note = tree.getroot()

items = note.find("body").find("items")
covid_list = []

# 컬럼 이름을 가져오는 함수
def get_record_column_names(items):
    for item in items.iter("item"):
        column_list = []
        is_first = True

        for column in item.iter():
            if is_first:
                is_first = False
                continue
            column_list.append(column.tag)

    print(column_list)




# 실데이터 레코드를 반환하는 함수
#def get_all_records(items):

df = get_record_column_names(items)
print(df)

