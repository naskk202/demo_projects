nums = [int(i) for i in input().split(" ")]
remover = int(input())
for i in range(remover):
    nums.remove(min(nums))
print(nums)
# for i in nums:
#     print(i, end = " ")