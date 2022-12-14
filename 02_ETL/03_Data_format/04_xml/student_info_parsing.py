from xml.etree.ElementTree import parse
from xml.etree.ElementTree import dump

def whole_xml():
    tree = parse("students_info.xml")
    note = tree.getroot()

    for parent in note.iter("student"):
        print("\n*",parent.get("name"))
        print("- 성별:",parent.get("sex"))
        print("- 나이:",parent.find("age").text)
        print("- 전공:",parent.find("major").text)

        # for child in parent.iter("language"):
        #     name = child.get("name")
        #     level = child.get("level")
        #     for child2 in parent.iter("period"):
        #         value = child2.get("value")
        #     print(f"=> {name} 학습기간: {value}, level: {level}")

        for child in parent:
            for child2 in child:
                print("=>",child2.get("name"),
                      "학습기간:",child2.find("period").get("value"),", level:",child2.get("level"))


def sumup_xml():
    tree = parse("students_info.xml")
    note = tree.getroot()




while True:
    print("\nXML데이터 분석 시작 ...")
    print("(1. 요약정보 / 2. 전체데이터 조회 / 3. 종료)")
    select = int(input("메뉴 입력 : "))

    if select == 1:
        sumup_xml()

    elif select == 2:
        whole_xml()

    elif select == 3:
        print("학생 정보 분석 완료!")
        quit()
