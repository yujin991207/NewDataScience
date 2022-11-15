link_stack = []

print(link_stack)
link_stack.append("메인화면")
print(link_stack)
link_stack.append("상품조회화면")
print(link_stack)
link_stack.append("주문화면")
print(link_stack)

link_stack.pop() # 마지막거부터 처리해준다
print(link_stack)
link_stack.pop()
print(link_stack)