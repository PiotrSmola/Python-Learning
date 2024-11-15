print("#############\n")
def dekoruj(wzor):
    def oblicz():
        a = 4
        b = 5
        wzor(a, b)
        print(a+b)
    return oblicz

def wzor(a, b):
    print(str(a) + " + " + str(b))

decor = dekoruj(wzor)
decor()