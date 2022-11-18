#3
import sys

nums = sys.argv[1:]

def num_allAdd(nums):
    sum = 0  # 지역변수
    for num in nums:
        #print(num)
        sum += int(num) # str이니깐 변환

        return sum


result = num_allAdd(nums)
print(result)