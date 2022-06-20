from collections import deque
import sys
from io import StringIO

input1 = """5, 6, 4, 16, 11, 5, 30, 2, 3, 27
1, 13, 5, 3, -7, 32, 19, 3, 5, 7, 22
"""

input2 = """-15, -8, 0, -16, 0, -22
10, 5
"""

sys.stdin = StringIO(input1)

fireworks = deque(int(i) for i in input().split(", "))
power = [int(i) for i in input().split(", ")]
palms_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
we_have_show = False

while fireworks and power:
    cur_firework = fireworks[0]
    while cur_firework <= 0:
        fireworks.popleft()
        if fireworks:
            cur_firework = fireworks[0]
        else:
            break
    cur_power = power[-1]
    while cur_power <= 0:
        power.pop()
        if power:
            cur_power = power[-1]
        else:
            break
    if not fireworks or not power:
        break
    cur_sum = cur_firework + cur_power

    if cur_sum % 3 == 0 and not cur_sum % 5 == 0:
        palms_fireworks += 1
        fireworks.popleft()
        power.pop()
    elif not cur_sum % 3 == 0 and cur_sum % 5 == 0:
        willow_fireworks += 1
        fireworks.popleft()
        power.pop()
    elif cur_sum % 3 == 0 and cur_sum % 5 == 0:
        crossette_fireworks += 1
        fireworks.popleft()
        power.pop()
    else:
        fireworks.popleft()
        fireworks.append(cur_firework - 1)
    if palms_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        we_have_show = True
        break

if we_have_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join(str(i) for i in fireworks)}")

if power:
    print(f"Explosive Power left: {', '.join(str(i) for i in power)}")

print(f"Palm Fireworks: {palms_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")