country = input().split(", ")
capitals = input().split(", ")
my_dict = zip(country, capitals)
for k, v in my_dict:
    print(f"{k} -> {v}")
