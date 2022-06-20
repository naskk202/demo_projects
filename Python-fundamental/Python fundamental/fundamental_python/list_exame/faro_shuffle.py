cards = input().split(" ")
num_of_shuffle = int(input())
shuff_deck = cards[1:-1]
empty1 = []
empty2 = []
for shuffle in range(num_of_shuffle):
    for card in range(len(shuff_deck)):
        if card < len(cards) / 2 - 1:
            empty1.append(shuff_deck[card])
        else:
            empty2.append(shuff_deck[card])
    shuff_deck = []
    for new in range(len(empty1)):
        shuff_deck.append(empty2[new])
        shuff_deck.append(empty1[new])
    empty1 = []
    empty2 = []
shuff_deck.insert(0, cards[0])
shuff_deck.append(cards[-1])
print(shuff_deck)






# cards = input().split(" ")
# num_of_shuffle = int(input())
# shuff_deck = cards[1:-1]
# empty1 = []
# empty2 = []
# for shuffle in range(num_of_shuffle):
#     empty1 = shuff_deck[0:int(len(shuff_deck) / 2)]
#     empty2 = shuff_deck[int(len(shuff_deck) / 2)::]
#     shuff_deck = []
#     for new in range(len(empty1)):
#         shuff_deck.append(empty2[new])
#         shuff_deck.append(empty1[new])
#     empty1 = []
#     empty2 = []
# shuff_deck.insert(0, cards[0])
# shuff_deck.append(cards[-1])
# print(shuff_deck)
