# 1. mumltiplication_function

# def multiply(*args):
#     smu = 1
#     for i in args:
#         smu *= i
#     return smu
#
#
# print(multiply(1, 4, 5))
# print(multiply(4, 5, 6, 1, 3))
# print(multiply(2, 0, 1000, 5000))


# 2. person_info


# def get_info(**kwargs):
#     if not kwargs:
#         return None
#     return f"This is {kwargs['name']} from {kwargs['town']} and he is {kwargs['age']} years old"
#
#
# print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))


# 3. character_permutations

# def permutation(text, cur_index):
#     if cur_index >= len(text):
#         print(text)
#         return
#     permutation(text, cur_index + 1)
#     for i in range(cur_index + 1, len(text)):
#         text[cur_index], text[i] = text[i], text[cur_index]
#         permutation(text, cur_index + 1)
#         text[cur_index], text[i] = text[i], text[cur_index]
#
# test = list(input())
# permutation(test, 0)


# def permutation(text, cur_index):
#     if cur_index >= len(text):
#         print(text)
#         return
#     permutation(text, cur_index + 1)
#     for i in range(cur_index + 1, len(text)):
#         text[cur_index], text[i] = text[i], text[cur_index]
#         permutation(text, cur_index + 1)
#         text[cur_index], text[i] = text[i], text[cur_index]
#
#
# text = list(input())
# permutation(text, 0)


# 4. chairs


# def chairs_combo(people, cur_index, chairs, combo):
#     if len(combo) == chairs:
#         print(", ".join(combo))
#         return
#     for i in range(cur_index, len(people)):
#         combo.append(people[i])
#         chairs_combo(people, i + 1, chairs, combo)
#         combo.pop()
#
#
# people = input().split(", ")
# chairs = int(input())
#
# chairs_combo(people, 0, chairs, [])
#
# def factorial(num):
#     if num < 2:
#         return 1
#     else:
#         return num * factorial(num - 1)
#
# num = 5
# print(factorial(num))


# 5. operator


# def operate(sign, *args):
#     result = 0
#     if sign ==
#
#
# print(operate("-", 0, 3, 4, 7, 8))
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))
# print(operate("/", 0, 3, 4, 7))


# 6. expressions


# def expression(nums, cur_index, express):
#     if len(express) == len(nums):
#         print(express)
#         return
#     for i in range(cur_index, len(express)):
#         express.append(nums[i])
#
#
#
#
#
# nums = [int(i) for i in input().split(", ")]
#
# print(expression(nums, 0, []))