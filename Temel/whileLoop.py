# -*- coding: utf-8 -*-

sayac = 1
sonuc = 0
while sayac <= 100:
    sonuc = sonuc + sayac
    sayac = sayac + 1
    print(sonuc)
    if sayac == 11:
        print("Sonsuz döngü koruması aktif!")
        break
    
print("1'den",sayac-1,"'a kadar olan sayıların toplamı : ",sonuc)
    