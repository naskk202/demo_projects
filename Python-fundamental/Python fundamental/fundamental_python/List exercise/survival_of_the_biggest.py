nums = [int(i) for i in input().split(" ")]
remover = int(input())
for i in range(remover):
    nums.remove(min(nums))
for i in range(len(nums)):
    if i == len(nums) - 1:
        print(nums[i])
    else:
        print(nums[i], end = ", ")