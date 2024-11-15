class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __str__(self):
        return f'Osoba: {self.imie} {self.nazwisko}'

class Student(Osoba):
    def __init__(self, imie, nazwisko, numer_albumu):
        super().__init__(imie, nazwisko)
        self.numer_albumu = numer_albumu

    def __str__(self):
        return f'Student: {self.imie} {self.nazwisko}, Numer Albumu: {self.numer_albumu}'

student1 = Student("Jan", "Kowalski", "123456")
student2 = Student("Andrzej", "Nowak", "234567")
student3 = Student("Piotr", "Malinowski", "345678")

print(student1)
print(student2)
print(student3)