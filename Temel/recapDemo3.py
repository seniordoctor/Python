# -*- coding: utf-8 -*-


sayi = int(input("Lütfen sayı giriniz : "))
asalMi = True


for x in range(2,sayi):
    if sayi % x == 0:
        asalMi = False
        break
    
    
if asalMi == True:                  # ve if asalMi: yaparsak default olarak True değerini alacaktır.
    print("ASAL")
else:
    print("ASAL DEĞİL")
    