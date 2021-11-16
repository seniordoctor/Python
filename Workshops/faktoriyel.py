# -*- coding: utf-8 -*-


sayi = int(input("Hangi sayının faktoriyelini istersiniz : "))

faktoriyel = 1

if sayi < 0:
    print("Negatif Sayıların Faktoriyeli Hesaplanamaz.")
elif sayi == 0:
    print("Sonuç : 1")
else:
    for i in range(1,sayi+1):
        faktoriyel = faktoriyel * i
        print(sayi ,"sayısının faktoriyeli: ", faktoriyel)












