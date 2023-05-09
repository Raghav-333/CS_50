import random


# coin = random.choice(['Heads' , 'Tails'])
# print(coin)
# # random.choice picks a random item from a list of items.







# number = random.randint(1 , 10)
# print(number)
# # 'random.randint' function return an integer between the two values







cards = ['Jack' , 'Queen' , 'King']
random.shuffle(cards)
print(cards)
for card in cards:
    print(card)
# 'random.shuffle' shuffles a given list.