from xml.etree.ElementTree import parse
import pandas as pd

output_file = "student_info_parsing.csv"

def student_xml_to_df():
    tree = parse("students_zero.xml")
    note = tree.getroot()

    student_row_list = []
    column_list = ['이름', '성별', '나이', '전공']

    for parent in note.iter("student"):
        name = parent.get("name")
        sex = parent.get("sex")
        age = parent.find("age").text
        major = parent.find("major").text

        student_row_list.append({"이름": name,"성별": sex,
                                 "나이": age, "전공": major})

    student_list = pd.DataFrame(student_row_list, columns = column_list)
    student_list.to_csv(output_file, index = False, encoding = 'cp949')
    print(student_list)


student_xml_to_df()




