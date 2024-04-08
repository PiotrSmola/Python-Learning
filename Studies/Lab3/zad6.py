import random


def deck():
    kolory = ['c', 'd', 'h', 's']
    rangi = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    cards = [(ranga, kolor) for ranga in rangi for kolor in kolory]
    return cards


def shuffle_deck(deck):
    random.shuffle(deck)


def deal(deck, n):
    rozdane = []
    for i in range(n):
        taliaGracza = []
        for j in range(5):
            index = random.randint(0, len(deck) - 1)
            taliaGracza.append(deck[index])
            deck.remove(deck[index])
        rozdane.append(taliaGracza)
    return rozdane


talia = deck()
print(talia, "\n")
shuffle_deck(talia)
print(talia, "\n")
print(deal(talia, 10))
