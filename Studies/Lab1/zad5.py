import datetime
dzisiaj = datetime.date.today()
print(dzisiaj)
wprowadzonaData = input("Podaj datę w formacie rrrr-mm-dd ")
wybranaData = datetime.datetime.strptime(wprowadzonaData, "%Y-%m-%d").date()
print(wybranaData)
roznicaDat = dzisiaj-wybranaData
print(roznicaDat.days)