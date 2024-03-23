import random


def lotto():
    liczba = random.sample(range(1,50), 6)
    return liczba

print("Wylosowane liczby: ", lotto())
