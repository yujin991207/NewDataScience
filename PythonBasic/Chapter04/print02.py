order_queue = []

print(order_queue)
order_queue.append("주문번호 0001")
print(order_queue)
order_queue.append("주문번호 0002")
print(order_queue)
order_queue.append("주문번호 0003")
print(order_queue)

order_queue.pop(0) # 먼저 들어온것부터 처리
print(order_queue)
order_queue.pop(0)
print(order_queue)
order_queue.pop(0)
print(order_queue)