# -*- coding: utf-8 -*-
                                   # Union işlemini yapınca olan sayılar veya karakterler aynı ise yazılmaz
setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB)                 # Union yapmış olduk.
print(setA.union(setB))             # diğer bir union yapma taktiği
print(setB.union(setA)) 

print(setA & setB)                # ortak olanları değerleri gösteriyor.
print(setA.intersection(setB))             
print(setB.intersection(setA)) 

print(setA - setB)                 # A'nın B'den farkı
print(setA.difference(setB))             
print(setB.difference(setA)) 

print(setA ^ setB)                 # 2 grubunda birbirinden farkını verir.
print(setA.symmetric_difference(setB))             
print(setB.symmetric_difference(setA)) 