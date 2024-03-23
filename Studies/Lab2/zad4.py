import math

print("########### KALKULATOR ###########")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Potęgowanie")
print("6. Pierwiastkowanie")
print("7. Pole koła")
print("8. Obwód koła")
print("9. Wyjście")
print("##################################\n")


def dodawanie(a, b):
    print("Wynik dodawania liczb ", a, "i", b, "wynosi", (a + b))


def odejmowanie(a, b):
    print("Wynik odejmowania liczb ", a, "i", b, "wynosi", (a - b))


def mnozenie(a, b):
    print("Wynik mnożenia liczb ", a, "i", b, "wynosi", (a * b))


def dzielenie(a, b):
    print("Wynik dzielenia liczb ", a, "i", b, "wynosi", (a / b))


def potegowanie(a, b):
    print("Wynik potęgowania liczb ", a, "i", b, "wynosi", (a ** b))


def pierwiastkowanie(a):
    print("Wynik pierwiastkowania liczby ", a, "wynosi", (a ** 0.5))


def pole(r):
    print("Pole koła o promieniu", r, "wynosi: ", (math.pi * r ** 2))


def obwod(r):
    print("Obwód koła o promieniu", r, "wynosi: ", (2 * math.pi * r))


while True:
    wybor = int(input("Wybierz działanie lub opcję wyjścia z programu: "))
    if (wybor == 1 or wybor == 2 or wybor == 3 or wybor == 4 or wybor == 5):
        a = int(input("Podaj pierwszą cyfrę: "))
        b = int(input("Podaj drugą cyfrę: "))
    elif wybor == 6:
        a = int(input("Podaj cyfrę: "))
    elif (wybor == 7 or wybor == 8):
        r = int(input("Podaj promień koła: "))
    elif wybor == 9:
        print("Do zobaczenia! Koniec programu")
        break

    if wybor == 1:
        dodawanie(a, b)

    elif wybor == 2:
        odejmowanie(a, b)

    elif wybor == 3:
        mnozenie(a, b)

    elif wybor == 4:
        if b == 0:
            print("Nie można dzielić przez 0")
        else:
            dzielenie(a, b)

    elif wybor == 5:
        potegowanie(a, b)

    # w poprzednim laboratorium miałem funkcję pierwiastkowania więc ją również implementuję pomimo iż nie przyjmie funkcja dwóch parametrów jak to jest dane w treści zadania
    elif wybor == 6:
        if a < 0:
            print("Nie można pierwiastkować liczb ujemnych")
        else:
            pierwiastkowanie(a)

    elif wybor == 7:
        if r <= 0:
            print("Promień koła nie może być mniejszy bądź równy 0")
        else:
            pole(r)
    elif wybor == 8:
        if r <= 0:
            print("Promień koła nie może być mniejszy bądź równy 0")
        else:
            obwod(r)
    else:
        print("Nie ma takiej opcji")
