target = 0
while target < 10000:
    steps = input()
    if steps == "Going home":
        steps = int(input())
        target += steps
        break
    steps = int(steps)
    target += steps
if target < 10000:
    print(f"{10000 - target} more steps to reach goal.")
else:
    print(f"Goal reached! Good job!\n"
          f"{target - 10000} steps over the goal!")