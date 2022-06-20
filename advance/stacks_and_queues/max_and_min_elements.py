from collections import deque

queue = deque()

for q in range(int(input())):
    command = input()
    if command.startswith("1"):
        queue.append(int(command.split()[1]))
    else:
        if queue:
            if command == "2":
                queue.pop()
            elif command == "3":
                print(max(queue))
            elif command == "4":
                print(min(queue))

rev_q = []

while queue:
    rev_q.append(str(queue.pop()))
print(", ".join(rev_q))