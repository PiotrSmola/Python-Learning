word = 'spam'
lista = []

# def createList():
#     for letter in word:
#         yield letter
#         singleWord = word[:1] + letter + word[1:]
#         lista.append(singleWord)

def createList():
    i = 1
    while i < len(word)+1:
        yield word[:i]
        i+=1

for i in createList():
    lista.append(i)

print(list(lista))