# -*- coding: utf-8 -*-

sayi1 = int(input("lütfen 1. sayıyı giriniz: "))
sayi2 = int(input("lütfen 2. sayıyı giriniz: "))
sayi3 = int(input("lütfen 3. sayıyı giriniz: "))

if (sayi1>=sayi2) and (sayi1>=sayi3):
    enBuyuk = sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3):
    enBuyuk = sayi2
else:
    enBuyuk = sayi3
    
print("En Büyük ", enBuyuk)