#8
# m은 게시물 갯수
# n 페이지당 보여줄 개수 : 10
def getTotalPage(m,n):
    if m % n != 0:
        totalpage = m // n
        totalpage += 1
        #print(totalpage)
    else:
        totalpage = m // n

    return totalpage

print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))