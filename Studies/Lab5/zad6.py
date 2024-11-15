class Dog:
    count = 0  # this is a class variable
    dogs = []  # this is a class variable

    def __init__(self, name):
        self.name = name  # self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):  # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def show_dogs():
        print(f'Liczba obiektów (piesków): {Dog.count}')
        print('Imiona wszystkich piesków:')
        for name in Dog.dogs:
            print(name)

dog1 = Dog("Reksio")
dog2 = Dog("Burek")
dog3 = Dog("Azor")

dog2.bark(9)

Dog.show_dogs()
