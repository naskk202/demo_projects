# 1. unique_usernames

# usernames = set()
#
# for _ in range(int(input())):
#     usernames.add(input())
#
# print("\n".join(usernames))


# 2. sets_of_elements

# one, two = input().split()
# first = set()
# second = set()
# for _ in range(int(one)):
#     first.add(input())
#
# for _ in range(int(two)):
#     second.add(input())
#
# third = "\n".join(first & second)
# print(third)

# 3. periodic_table

# elements = []
#
# for _ in range(int(input())):
#     components = set(input().split())
#     elements.extend(components)
#
# print("\n".join(set(elements)))

# 4. count_symbols

# text = input()
# my_dict = {}
#
# for i in text:
#     if i not in my_dict:
#         my_dict[i] = 0
#     my_dict[i] += 1
#
# sorted_my_dict = sorted(my_dict.items(), key=lambda x: x[0])
# for k, v in sorted_my_dict:
#     print(f"{k}: {v} time/s")

# 5. longest_intersection

# def indexes(ranges):
#     set = []
#     start, end = ranges.split(",")
#     for i in range(int(start), int(end) + 1):
#         set.append(i)
#     return set
#
#
# longest_intersection = []
#
# for _ in range(int(input())):
#     first, second = input().split("-")
#     first_set = set(indexes(first))
#     second_set = set(indexes(second))
#     intersection = first_set & second_set
#     if len(intersection) > len(longest_intersection):
#         longest_intersection = [i for i in sorted(intersection)]
# print(f'Longest intersection is {longest_intersection} with length {len(longest_intersection)}')

# 6. battle_of_names

# odd_names = set()
# even_names = set()
# for i in range(int(input())):
#     name = input()
#     sum_name = int(sum([ord(i) for i in name]) / (i + 1))
#     if sum_name % 2 == 0:
#         even_names.add(sum_name)
#     else:
#         odd_names.add(sum_name)
# sum_even = sum(even_names)
# sum_odd = sum(odd_names)
# # print(odd_names)
# # print(even_names)
# # print(sum_odd)
# # print(sum_even)
# if sum_odd == sum_even:
#     print(odd_names ^ even_names)
# elif sum_odd > sum_even:
#     print(", ".join(reversed([str(i) for i in odd_names])))
# else:
#     print(", ".join(str(i) for i in (odd_names ^ even_names)))
