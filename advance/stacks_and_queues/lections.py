# string = list(input())
# reversed_list = []
#
# while string:
#     a = string.pop()
#     reversed_list.append(a)
# print("".join(reversed_list))


# pattern = input()
#
# parentheses_index = []
#
# for index in range(len(pattern)):
#     if pattern[index] == "(":
#         parentheses_index.append(index)
#     elif pattern[index] == ")":
#         start_parentheses = parentheses_index.pop()
#         print(pattern[start_parentheses:index + 1])


# from collections import deque
#
# name = input()
# queue = deque()
#
# while not name == "End":
#     if name == "Paid":
#         while queue:
#             print(queue.popleft())
#     else:
#         queue.append(name)
#     name = input()
# print(f"{len(queue)} people remaining.")


# from collections import deque
#
#
# quantity_of_water = int(input())
# name = input()
# queue = deque()
#
# while not name == "Start":
#     queue.append(name)
#     name = input()
#
# command = input()
# while not command == "End":
#     if "refill" in command:
#         quantity_of_water += int(command.split()[1])
#     else:
#         name = queue.popleft()
#         if int(command) <= quantity_of_water:
#             print(f"{name} got water")
#             quantity_of_water -= int(command)
#         else:
#             print(f"{name} must wait")
#     command = input()
# print(f"{quantity_of_water} liters left")


# from collections import deque
#
# group = deque(input().split())
# turns = int(input())
#
# while len(group) > 1:
#     group.rotate(-turns)
#     print(f"Removed {group.pop()}")
# print(f"Last is {group.pop()}")




# from collections import deque
#
# a = deque([1, 2, 3, 4, 5, 6])
# a.rotate(1)
# print(a)
# a.rotate(-2)
# print(a)
# a.rotate(1)
# print(a)
# a.rotate()
# print(a)