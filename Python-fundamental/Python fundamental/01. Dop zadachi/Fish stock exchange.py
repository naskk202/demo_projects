mackerel_price = float(input())
sprat_price = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = float(input())
bonito_price = (mackerel_price + (mackerel_price * 0.6)) * bonito_kg
horse_mackerel_price = (sprat_price + (sprat_price * 0.8)) * horse_mackerel_kg
mussels_price = mussels_kg * 7.5
sum = bonito_price + horse_mackerel_price + mussels_price
print(round(sum, 2))