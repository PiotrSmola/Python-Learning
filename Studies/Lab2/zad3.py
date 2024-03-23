print("########### KALKULATOR ###########")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Potęgowanie")
print("6. Pierwiastkowanie")
print("7. Wyjście")
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


while True:
    wybor = int(input("Wybierz działanie lub opcję wyjścia z programu: "))
    if (wybor == 1 or wybor == 2 or wybor == 3 or wybor == 4 or wybor == 5):
        a = int(input("Podaj pierwszą cyfrę: "))
        b = int(input("Podaj drugą cyfrę: "))
    elif wybor == 6:
        a = int(input("Podaj cyfrę: "))
    elif wybor == 7:
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
    else:
        print("Nie ma takiej opcji")
