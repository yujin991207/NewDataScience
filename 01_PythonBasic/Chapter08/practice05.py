#5
candidate_list = []
file = open("data/연습생.txt", mode='r', encoding='utf-8')

names = file.readlines()
#print(names)

# 텍스트파일에있는 연습생이름을 꺼낸다
for name in names:
    candidate_list.append(name.strip())

def show_candidates(candidate_list):
    print(candidate_list)

def make_idol(candidate_list):
    for name in candidate_list:
        print(f'신예 아이돌 {name} 인기 급상승!')

def make_world_star(candidate_list):
    for name in candidate_list:
        print(f'아이돌 {name} 월드스타 등극!')

show_candidates(candidate_list)
print()
make_idol(candidate_list)
print()
make_world_star(candidate_list)
print()






