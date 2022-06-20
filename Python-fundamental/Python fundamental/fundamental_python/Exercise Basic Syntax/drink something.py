age = int(input())
drink = ""
if age < 15:
    drink = "toddy"
elif age < 19:
    drink = "coke"
elif age < 22:
    drink = "beer"
else:
    drink = "whisky"
print(f"drink {drink}")