class Liczba:
    def __init__(self, wartoscLiczbowa):
        self.wartosc = wartoscLiczbowa

    def __mul__(self, other):
        if isinstance(other, Liczba):
            x = self.wartosc
            y = other.wartosc
            return Liczba(x**2 + 2*x*y + y)
        else:
            raise ValueError("Mnożenie jest możliwe tylko między instancjami klasy Liczba")

    def __str__(self):
        return str(self.wartosc)

liczba1 = Liczba(7)
liczba2 = Liczba(3)

wynik = liczba1 * liczba2

print(f'Wynik działania {liczba1}^2 + 2*{liczba1}*{liczba2} +{liczba2} = {wynik}')
