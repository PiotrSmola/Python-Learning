print("########### KALKULATOR ###########")
print("1. Dodawanie")
print("2. Odejmowanie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5. Potęgowanie")
print("6. Pierwiastkowanie")
print("7. Wyjście")
print("##################################\n")

while True:
    wybor = int(input("Wybierz działanie: "))
    if wybor == 1:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        print("Wynik dodawania: ", a + b,"\n")

    elif wybor == 2:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        print("Wynik odejmowania: ", a - b,"\n")

    elif wybor == 3:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        print("Wynik mnożenia: ", a * b,"\n")

    elif wybor == 4:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        if b == 0:
            print("Nie można dzielić przez 0")
        else:
            print("Wynik dzielenia: ", a / b,"\n")

    elif wybor == 5:
        a = float(input("Podaj podstawę: "))
        b = float(input("Podaj wykładnik: "))
        print("Wynik potęgowania: ",a ** b,"\n")

    elif wybor == 6:
        a = float(input("Podaj liczbę: "))
        if a < 0:
            print("Nie można pierwiastkować liczb ujemnych")
        else:
            print("Wynik pierwiastkowania: ", a ** 0.5,"\n")

    elif wybor == 7:
        print("Do zobaczenia! Koniec programu")
        break
    else:
        print("Nie ma takiej opcji")
