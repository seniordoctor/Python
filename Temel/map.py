

sayilar = [1,2,3,4,5]               #array'in karesini almak istiyoruz

sayilarKareli = list(map(lambda sayi: sayi*2,sayilar))

# for sayi in sayilar:
#     sayilarKareli.append(sayi*sayi)

sayilarFiltreli = list(filter(lambda sayi : sayi>2,sayilar))                    # sayilar listesinde sayi eğer 2'den büyükse yaz.

print("Filtre : ",sayilarFiltreli)
print("Kareli : ",sayilarKareli)

from functools import reduce
sayilarFaktoriyel = reduce(lambda x,y:x*y,sayilar)

print("Faktoriyel : ",sayilarFaktoriyel)