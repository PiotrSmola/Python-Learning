print('Hello world!')
print(2 + 2)
print(5 - 2 + 4)
print((-7 + 2) * (-4))
# print(6/0)

print("spam\t" * 4)
print("Jeden" + " dwa")
a = "Welcome to Python's world!"
print(a[0])
print(a[0:7])

wiek = input("Podaj wiek: ")
print(wiek)

x = 7
print(x)
print(x + 3)
print(x)

x = 2
if x != 2:
    print('tak')

x = 123
print(x)
x = "To jest napis"
print(x + "!")

foo = "napis"
print(foo)
# print(bar)
del foo
# print(foo)

if 10 > 5:
    print("10 jest większe od 5")
print("koniec skryptu")

num = int(input("podaj liczbę: "))
if num > 5:
    print("Większa niż 5")
    if num <= 45:
        print("Wartość z przedziału (5; 45]")

x = 4
if x == 5:
    print("Tak")
else:
    print("Nie")

num = 25
if num == 5:
    print("Numerem jest 5")
else:
    if num == 15:
        print("Numerem jest 15")
    else:
        print("Numerem nie jest 5 ani 15")

num = 7
if num == 5:
    print("Numerem jest 5")
elif num == 10:
    print("Numerem jest 10")
elif num == 7:
    print("Numerem jest 7")
else:
    print("Numerem nie jest 5, 10 ani 7")

i = 1
while i <= 50:
    print(i)
    i = i + 1
print("Koniec!")

# while 1 == 1:
#   print("operacje w pętli")

i = 0
while True:
    print(i)
    i = i + 1
    if i >= 10:
        print("Przerwanie")
        break
print("Koniec")

i = 0
while 1 == 1:
    i = i + 1
    if i == 2:
        print("Pomiń 2")
        continue
    if i == 7:
        print("Przerwanie")
        break
    print(i)
print("Koniec")

words = ["Hello", "world", ".!"]
print(words[0])
print(words[1])
print(words[2])

number = 3
things = ["string", 0, [1, 2, number], 3.14]
print(things[1])
print(things[2])
print(things[2][2])

nums = [7, 1, 1, 7]
nums[2] = 5
print(nums)

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 5)

words = ["spam", "egg"]
print("spam" in words)
print("potatoes" in words)

nums = [1, 2, 3]
print(not 4 in nums)
print(5 not in nums)
print(not 3 in nums)
print(6 not in nums)

nums = [1, 2, 3]
nums.append(4)
print(nums)
print(len(nums))
nums.append(5)
nums.append(6)
print(nums)
print(len(nums))

words = ['Python', 'cool']
words.insert(1, 'is')
words.insert(3, "and easy")
print(words)

letters = ['q', 'w', 'e', 'r', 't', 'y']
print(dir(letters))
if (letters.index('w') == True):
    print("Znaleziono w")
# Jak obsłużyć nieodnalezienie elementu, aby nie kończyło się to błędem i przerwaniem skryptu?
# if (letters.index('m') == True):
#     print("Znaleziono m")
# else:
#     print("Nie znaleziono m")
print(max(letters))
print(letters.count('e'))
letters.remove('q')
print(letters)
letters.reverse()
print(letters)
letters.sort()
print(letters)
letters.pop(3)
print(letters)
letters.extend(words)
print(letters)

words = ["hello", "world", "cheese", "eggs"]
for word in words:
  print(word + "!")

for i in range(10):
  print(i)



