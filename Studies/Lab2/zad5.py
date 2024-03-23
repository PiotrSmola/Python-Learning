def suma(lista):
    sumaLiczb=0
    for i in lista:
        i = int(i)
        sumaLiczb = sumaLiczb + i
    print("Suma: ", sumaLiczb)


def odczytLiczb(func):
    file = open("liczby.txt", "r")
    suma(file.readlines())
    file.close()

odczytLiczb(suma)