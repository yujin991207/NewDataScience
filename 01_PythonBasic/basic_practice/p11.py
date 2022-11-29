#11
import random

student_list = ['김유진','김지혜','문성준','박종민','송지예','양석훈','이예지','임성혁','한권제','현재봉','이현구']

def coffe_lotto(student_list,target_num):
    #target_num = int(input('\n당첨자 수를 입력하세요 : '))
    choice_student = random.sample(student_list,target_num)
    print(f'축하합니다! {choice_student}님 당첨되셨습니다!\n')

def presentation_order(student_list):
    student_list = student_list[0:10]
    random.shuffle(student_list)
    print('\n발표자 순서는 아래와 같습니다')
    print(f'{student_list}\n')

while True:
    menu = input('메뉴를 선택하세요 1.커피로또 2.발표순서 (엔터 => 종료) : ')

    if menu == '':
        break

    elif menu == '1':
        target_num = int(input('\n당첨자 수를 입력하세요 : '))
        coffe_lotto(student_list,target_num)

    elif menu == '2':
        presentation_order(student_list)




