from xml.etree.ElementTree import parse
import pandas as pd

def get_record_column_names(records):
    for record in records.iter("record"):
        column_list = []
        is_first = True
        for column_data in record.iter():
            if is_first:
                is_first = False
                continue
            column_list.append(column_data.tag)

        return column_list

def get_all_records(records):

    all_records = []
    for record in records.iter("record"):

        simple_row_list=[] # 행 데이터

        is_first = True
        for column_data in record.iter():
            if is_first:
                is_first = False
                continue
            simple_row_list.append(column_data.text)
        all_records.append(simple_row_list)

    return all_records


tree = parse("전국폐교재산기본정보표준데이터.xml")
dataGrid = tree.getroot()
records = dataGrid.find('records').find('record')



print(get_record_column_names(records))

all_records = get_all_records(records)
column_list = get_record_column_names(records)
print(all_records)
print(column_list)
df = pd.DataFrame(all_records, columns=column_list)
df.to_csv('전국폐교재산기본정보표준데이터_v1.csv', encoding='utf-8', index=False)