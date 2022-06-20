# def to_pr(classification):
#     a = ""
#     for i in classification:
#         if i == classification[-1]:
#             a += str(i)
#         else:
#             a += str(i) + ", "
#     return a
#
#
# nums = list(map(int, input().split(", ")))
# positive = [i for i in nums if i >= 0]
# negative = [i for i in nums if i < 0]
# even = [i for i in nums if i % 2 == 0]
# odd = [i for i in nums if not i % 2 == 0]
# print(f"Positive: {to_pr(positive)}\n"
#       f"Negative: {to_pr((negative))}\n"
#       f"Even: {to_pr(even)}\n"
#       f"Odd: {to_pr(odd)}")


#
# def to_pr(classification):
#     a = ""
#     for i in classification:
#         if i == classification[-1]:
#             a += str(i)
#         else:
#             a += str(i) + ", "
#     return a


# nums = list(map(int, input().split(", ")))
# positive = "".join(str(i) + ", " if i >= 0 and not i == nums[-1] else  for i in nums)
# negative = [i for i in nums if i < 0]
# even = [i for i in nums if i % 2 == 0]
# odd = [i for i in nums if not i % 2 == 0]
# print(f"Positive: {positive}\n"
#       f"Negative: {(i for i in negative)}\n"
#       f"Even: {(i for i in even)}\n"
#       f"Odd: {(i for i in odd)}")


nums = [int(i) for i in input().split(", ")]
pos_str = ", ".join(str(i) for i in nums if i >= 0)
neg_str = ", ".join(str(i) for i in nums if i < 0)
even_str = ", ".join(str(i) for i in nums if i % 2 == 0)
odd_str = ", ".join(str(i) for i in nums if not i % 2 == 0)
print(f"Positive: {pos_str}\n"
      f"Negative: {neg_str}\n"
      f"Even: {even_str}\n"
      f"Odd: {odd_str}")
