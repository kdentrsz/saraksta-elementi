def izdruka(daudzums, sarl):
  for elem in range(0, daudzums):
    print(sarl[elem])
  return 0

saraksts = [2,4,5,6,1,2,34,5]
daudzums = int(input("Ievadi elementu skaitu:"))
rez = izdruka(daudzums, saraksts)