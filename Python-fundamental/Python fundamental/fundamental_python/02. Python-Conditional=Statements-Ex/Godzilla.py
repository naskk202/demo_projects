budget = float(input())
actors = int(input())
dress_price= float(input())
if actors > 150:
    dress = (dress_price * actors) * 0.9
else:
    dress = dress_price * actors
decor = budget * 0.1
if decor + dress > budget:
    print(f"""
Not enough money!
Wingard needs {(decor + dress) - budget:.2f} leva more.    
""")
else:
    print(f"""
Action!
Wingard starts filming with {budget - (decor + dress):.2f} leva left.
""")