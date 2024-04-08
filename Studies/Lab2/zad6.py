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


# Usprawniłem nieco uprzedni program dodając warunki dla wybranych opcji jako zbiór wartości, które mogą być wybrane oraz zamiast przecinków czy plusów użyłem f-stringów gdyż są szybsze i bardziej czytelne
def zapisz_do_pliku(tekst):
    with open("./wyniki.txt", "a") as plik:
        plik.write(tekst + "\n")


def dodawanie(a, b):
    wynik = f"Wynik dodawania liczb {a} i {b} wynosi {a + b}"
    print(wynik)
    return wynik


def odejmowanie(a, b):
    wynik = f"Wynik odejmowania liczb {a} i {b} wynosi {a - b}"
    print(wynik)
    return wynik


def mnozenie(a, b):
    wynik = f"Wynik mnożenia liczb {a} i {b} wynosi {a * b}"
    print(wynik)
    return wynik


def dzielenie(a, b):
    wynik = f"Wynik dzielenia liczb {a} i {b} wynosi {a / b}"
    print(wynik)
    return wynik


def potegowanie(a, b):
    wynik = f"Wynik potęgowania liczb {a} i {b} wynosi {a ** b}"
    print(wynik)
    return wynik


def pierwiastkowanie(a):
    wynik = f"Wynik pierwiastkowania liczby {a} wynosi {a ** 0.5}"
    print(wynik)
    return wynik


def pole(r):
    wynik = f"Pole koła o promieniu {r} wynosi: {math.pi * r ** 2}"
    print(wynik)
    return wynik


def obwod(r):
    wynik = f"Obwód koła o promieniu {r} wynosi: {2 * math.pi * r}"
    print(wynik)
    return wynik


while True:
    wybor = int(input("Wybierz działanie lub opcję wyjścia z programu: "))
    if wybor == 9:
        print("Koniec programu")
        break

    if wybor in [1, 2, 3, 4, 5]:
        a = int(input("Podaj pierwszą cyfrę: "))
        b = int(input("Podaj drugą cyfrę: "))
    elif wybor == 6:
        a = int(input("Podaj cyfrę: "))
    elif wybor in [7, 8]:
        r = int(input("Podaj promień koła: "))

    wynik_operacji = None

    if wybor == 1:
        wynik_operacji = dodawanie(a, b)
    elif wybor == 2:
        wynik_operacji = odejmowanie(a, b)
    elif wybor == 3:
        wynik_operacji = mnozenie(a, b)
    elif wybor == 4:
        if b == 0:
            print("Nie można dzielić przez 0")
        else:
            wynik_operacji = dzielenie(a, b)
    elif wybor == 5:
        wynik_operacji = potegowanie(a, b)
    elif wybor == 6:
        if a < 0:
            print("Nie można pierwiastkować liczb ujemnych")
        else:
            wynik_operacji = pierwiastkowanie(a)
    elif wybor == 7:
        if r <= 0:
            print("Promień koła nie może być mniejszy bądź równy 0")
        else:
            wynik_operacji = pole(r)
    elif wybor == 8:
        if r <= 0:
            print("Promień koła nie może być mniejszy bądź równy 0")
        else:
            wynik_operacji = obwod(r)
    else:
        print("Podano nieistniejącą opcję. Spróbuj ponownie.")

    if wynik_operacji:
        zapis = input("Czy zapisać wynik do pliku? (tak/nie): ").lower()
        if zapis == "tak":
            zapisz_do_pliku(wynik_operacji)
            print("Wynik zapisano do pliku.")
