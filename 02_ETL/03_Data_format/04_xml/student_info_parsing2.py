from xml.etree.ElementTree import parse
import pandas as pd

#output_file = "student_info_parsing.csv"
student_list = []

tree = parse("students_zero.xml")
note = tree.getroot()

for parent in note.iter("student"):
    student_row = []

    student_row.append(parent.get("name"))
    student_row.append(parent.get("sex"))
    student_row.append(parent.find("age").text)
    student_row.append(parent.find("major").text)

    print(student_row)
    #student_list.append(student_row)


# column_list = ['이름', '성별', '나이', '전공']
#
# df = pd.DataFrame(student_list, columns = column_list)
# #student_list.to_csv(output_file, index = False, encoding = 'cp949')
# print(df)




