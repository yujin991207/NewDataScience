import pandas as pd
from xml.etree.ElementTree import parse

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

tree = parse("지진해일_긴급대피장소.xml")
data_root = tree.getroot()

column_list, all_data = xml_to_df(data_root,'row')

df = pd.DataFrame(all_data, columns = column_list)
df.to_csv('지진해일_긴급대피장소.csv', index = False)
print(df)

