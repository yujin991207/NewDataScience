# -*- coding: utf-8 -*-
from xml.etree.ElementTree import parse
import pandas as pd

def covid_xml_to_df():
    tree = parse("12월14일_코로나_예방접종현황.xml")
    note = tree.getroot()

    covid_list = []
    items = note.find("body").find("items")

    for item in items:

        row_list = []

        row_list.append(item.find("tpcd").text)
        row_list.append(item.find("firstCnt").text)
        row_list.append(item.find("secondCnt").text)
        row_list.append(item.find("thirdCnt").text)
        row_list.append(item.find("fourCnt").text)
        row_list.append(item.find("winCnt").text)
        row_list.append(item.find("vrate").text)
        row_list.append(item.find("wrate").text)

        covid_list.append(row_list)

    column_list = ['tpcd','firstCnt','secondCnt','thirdCnt','fourCnt','winCnt','vrate','wrate']
    return pd.DataFrame(covid_list, columns = column_list)

df = covid_xml_to_df()
print(df)

df.to_csv('12월14일_코로나_예방접종현황_v1.csv', encoding = 'cp949', index = False)