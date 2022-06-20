change = float(input())
coins = 0
change_in_coins = change * 100
coins += change_in_coins // 200
coins += (change_in_coins % 200) // 100
coins += ((change_in_coins % 200) % 100) // 50
coins += (((change_in_coins % 200) % 100) % 50) // 20
coins += ((((change_in_coins % 200) % 100) % 50) % 20) // 10
coins += (((((change_in_coins % 200) % 100) % 50) % 20) % 10) // 5
coins += ((((((change_in_coins % 200) % 100) % 50) % 20) % 10) % 5) // 2
coins += (((((((change_in_coins % 200) % 100) % 50) % 20) % 10) % 5) % 2) // 1
print(int(coins))