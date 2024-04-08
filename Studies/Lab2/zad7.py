import cmath


# Aby program był nieco "pełniejszy" oprócz rozwiązań rzeczywistych dodałem również rozwiązania zespolone
def rown_kwadrat(a, b, c):
    try:
        if a == 0:
            raise ValueError("To nie jest równanie kwadratowe, gdyż 'a' nie może być równe 0")
        delta = b ** 2 - 4 * a * c
        if delta >= 0:
            x1 = (-b - cmath.sqrt(delta)) / (2 * a)
            x2 = (-b + cmath.sqrt(delta)) / (2 * a)
            rozwiazania = f"Rzeczywiste rozwiązania: x1 = {x1.real:.5f}, x2 = {x2.real:.5f}"
        else:
            x1 = (-b - cmath.sqrt(delta)) / (2 * a)
            x2 = (-b + cmath.sqrt(delta)) / (2 * a)
            rozwiazania = f"Zespolone rozwiązania: x1 = {x1:.5f}, x2 = {x2:.5f}"
    except ValueError as e:
        rozwiazania = str(e)
    except Exception as e:
        rozwiazania = f"Nieoczekiwany błąd: {e}"

    with open("result.txt", "w") as plik:
        plik.write(rozwiazania)


print("Podaj współczynniki równania kwadratowego ax^2 + bx + c = 0: ")
a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
rown_kwadrat(a, b, c)
