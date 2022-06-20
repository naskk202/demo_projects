cards = input().split()
shuffles = int(input())
deck_one = cards
deck_two = []
for shuff in range(1, shuffles + 1):
    while len(deck_two) < len(deck_one):
        for i in range(1, len(deck_one) + 1):
            if i == 1:
                deck_two.append(deck_one[i - 1])
            elif len(deck_two) == len(deck_one) - 1:
                deck_two.append(deck_one[- 1])
                break
            else:
                deck_two.append(deck_one[len(deck_one) // 2 + i - 2])
                deck_two.append(deck_one[i - 1])
    deck_one = deck_two
    deck_two = []
print(deck_one)
