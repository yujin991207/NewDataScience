import json
import pandas as pd

def open_json(file_name, encoding):
    with open(file_name, encoding=encoding) as json_file:
        json_object = json.load(json_file)
        json_string = json.dumps(json_object)
        json_data = json.loads(json_string)
    return json_data

student_zero2 = open_json('student_zero2.json','cp949')

student_zero2

column_list = []
all_data = []

is_first = True

for student in student_zero2:
    row_data_list = []
    for key,value in student.items():
        if is_first:
            column_list.append(key)
        row_data_list.append(value)
    all_data.append(row_data_list)
    is_first = False

print(column_list)

student_data = pd.DataFrame(all_data, columns = column_list)

print(student_data)