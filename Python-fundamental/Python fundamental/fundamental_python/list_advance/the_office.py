employers = list(map(lambda x: int(x), input().split()))
factor = int(input())
employers = list(map(lambda x: x * factor, employers))
happiness = len([i for i in employers if i >= (sum(employers) / len(employers))])
if happiness >= len(employers) / 2:
    print(f"Score: {happiness}/{len(employers)}. Employees are happy!")
else:
    print(f"Score: {happiness}/{len(employers)}. Employees are not happy!")