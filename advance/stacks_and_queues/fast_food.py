from collections import deque


quantity = int(input())
a = [int(i) for i in input().split()]
print(max(a))
orders = deque()
for i in a:
    orders.append(str(i))

while orders:
    order = int(orders.popleft())
    if order <= quantity:
        quantity -= order
    else:
        orders.appendleft(str(order))
        break
if orders:
    print(f"Orders left: {' '.join(orders)}")
else:
    print("Orders complete")
