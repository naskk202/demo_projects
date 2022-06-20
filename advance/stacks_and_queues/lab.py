# 1. count_same_values

# nums = [float(i) for i in input().split()]
# pair_nums = {}
# for number in nums:
#     if number not in pair_nums:
#         pair_nums[number] = 0
#     pair_nums[number] += 1
# for k, v in pair_nums.items():
#     print(f"{k} - {v}


# 2. students_grades

# list = {}
#
# for i in range(int(input())):
#     name, grade = input().split()
#     grades = float(grade)
#     if name not in list:
#         list[name] = []
#     list[name].append(grades)
#
#
# for k, v in list.items():
#     name = k
#     average = sum(v) / len(v)
#     grades = " ".join(str(f"{i:.2f}") for i in v)
#     print(f"{name} -> {grades} (avg: {average:.2f})")

# 3. record_unique_names

# list = set()
#
# for i in range(int(input())):
#     list.add(input())
#
# for i in list:
#     print(i)

# 4. parking_lot
#
# parking = set()
#
# for i in range(int(input())):
#     direction, number = input().split(", ")
#
#     if direction == "IN":
#         parking.add(number)
#     else:
#         if number in parking:
#             parking.remove(number)
#
# if not parking:
#     print("Parking Lot is Empty")
# else:
#     for i in parking:
#         print(i)

# 5. soft_uni_party

# list = set()
# vip = set()
# reg = set()
# for i in range(int(input())):
#     list.add(input())
# while True:
#     command = input()
#     if command == "END":
#         break
#     list.remove(command)
#
# for i in list:
#     if i[0].isdigit():
#         vip.add(i)
#     else:
#         reg.add(i)
# print(len(list))
# if vip:
#     for i in sorted(vip):
#         print(i)
# if reg:
#     for i in sorted(reg):
#         print(i)

# 733, 512, 398, 618, 511, 609
# 733, 256, 133, 155, 102, 102
# 460, 1021
#
# a = sum([ord(i) for i in "Stefan"])
# print(a)