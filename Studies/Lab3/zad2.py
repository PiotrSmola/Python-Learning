from array import *

tablica = array('u',[])
tablica.extend(input("Podaj ciąg znaków dołączany do tablicy: ")) #raczej jest coś lepsze niż extend w tym przypadku
tablica.reverse()
print(tablica.tounicode())