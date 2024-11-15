def dzialaniaZbiory(zbior1, zbior2):
    print(zbior1 | zbior2)
    print(zbior1 & zbior2)
    print(zbior1 - zbior2)
    print(zbior1 ^ zbior2)

zbior1 = set([1, 3, 40, 4, 7, 9])
zbior2 = set([1, 256, 4, 5, 66, 7])
dzialaniaZbiory(zbior1, zbior2)