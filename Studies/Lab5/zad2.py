class Student:
    def __init__(self, imie, numer_albumu):
        self.imie = imie
        self.numer_albumu = numer_albumu

student1 = Student("Jan Kowalski", "123456")
student2 = Student("Andrzej Nowak", "234567")
student3 = Student("Piotr Malinowski", "345678")

print(student1.imie, student1.numer_albumu)
print(student2.imie, student2.numer_albumu)
print(student3.imie, student3.numer_albumu)
