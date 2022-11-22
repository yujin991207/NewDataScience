def solution(num1, num2):
    answer = 0
    if (0 <= num1 <= 100) and (0 <= num2 <=100):
      answer = num1 * num2
    return answer

print(solution(27,19))

def solution1(num1, num2):
    answer = 0
    if 0 <= num1 <= 10000 and 0 <= num2 <= 10000:
        if num1 == num2:
            print(1)
        elif num1 != num2:
            print(-1)
    return answer

print(solution1(2,3))

def solution2(age):
    answer = 0
    if 0 < age <= 120:
     answer = 2023 - age
    return answer

print(solution2(24))

def solution3(money):
    answer = []
    count = 0
    if 0 < money <= 1000000:
        count += 1
        answer = [money // 5500 , money - (5500 * (money // 5500))]
    return answer

print(solution3(15000))