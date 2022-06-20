nums = [int(i) for i in input().split(", ")]
num_lis = [i for i in range(len(nums)) if nums[i] % 2 == 0]
print(num_lis)
# nums = list(map(lambda x: int(x), input().split(", ")))