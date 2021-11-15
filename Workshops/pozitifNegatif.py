# -*- coding: utf-8 -*-

sayi = int(input("Bir sayı giriniz: "))

if sayi > 0:
    print("Girdiğiniz sayı pozitiftir.")
elif sayi == 0:
    print("Girdiğiniz sayı 0'dır.")
elif sayi < 0:
    print("Girdiğiniz sayı negatiftir.")
else:
    print("Lütfen bir sayı giriniz.")
